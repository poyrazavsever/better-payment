import { execFileSync } from 'node:child_process';
import { existsSync } from 'node:fs';
import { mkdir, readdir, readFile, stat, writeFile } from 'node:fs/promises';
import { dirname, extname, join, relative, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const toolDirectory = dirname(fileURLToPath(import.meta.url));
const root = resolve(toolDirectory, '..');
const vault = join(root, 'Better Payment Vault');
const mode = process.argv[2] ?? 'check';
const errors = [];
const requiredFrontmatter = ['tur', 'alan', 'guncelleme', 'ozet'];
const assetExtensions = new Set(['.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg', '.ico']);
const localPrefixes = [
  'Better Payment Vault/',
  '.local-tools/',
  '.local-githooks/',
  '.better-payment-local-ignore',
];
const vaultBranch = 'personal/vault';
const vaultRemoteRef = `refs/heads/${vaultBranch}`;
const vaultBranchFiles = ['README.md', '.gitignore', '.gitattributes'];

async function walk(directory) {
  const output = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    if (entry.name === '.obsidian') continue;
    const fullPath = join(directory, entry.name);
    if (entry.isDirectory()) output.push(...(await walk(fullPath)));
    else output.push(fullPath);
  }
  return output;
}

function display(path) {
  return relative(root, path).split(sep).join('/');
}

function parseFrontmatter(text) {
  const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return null;
  const fields = new Map();
  for (const line of match[1].split(/\r?\n/)) {
    const separator = line.indexOf(':');
    if (separator > 0) fields.set(line.slice(0, separator).trim(), line.slice(separator + 1).trim());
  }
  return fields;
}

function resolveWikiTarget(source, target, files) {
  const clean = target.split('|')[0].split('#')[0].trim();
  if (!clean) return true;
  const candidates = [
    resolve(vault, clean),
    resolve(vault, `${clean}.md`),
    resolve(source, clean),
    resolve(source, `${clean}.md`),
  ];
  if (candidates.some((candidate) => existsSync(candidate))) return true;
  const normalized = clean.replaceAll('\\', '/').toLowerCase();
  return files.some((file) => {
    const relativePath = relative(vault, file).split(sep).join('/').toLowerCase();
    return relativePath === normalized || relativePath === `${normalized}.md`;
  });
}

async function lint(files) {
  const markdown = files.filter((file) => extname(file).toLowerCase() === '.md');
  for (const file of markdown) {
    const text = await readFile(file, 'utf8');
    const frontmatter = parseFrontmatter(text);
    if (!frontmatter) {
      errors.push(`${display(file)}: missing frontmatter`);
      continue;
    }
    for (const field of requiredFrontmatter) {
      if (!frontmatter.get(field)) errors.push(`${display(file)}: missing frontmatter field '${field}'`);
    }
    if ((await stat(file)).size > 25 * 1024) {
      errors.push(`${display(file)}: exceeds 25 KB hot-note limit`);
    }
    for (const match of text.matchAll(/!?(?:\[\[)([^\]]+)\]\]/g)) {
      if (!resolveWikiTarget(dirname(file), match[1], files)) {
        errors.push(`${display(file)}: unresolved wiki link '${match[1]}'`);
      }
    }
  }
  console.log(`Vault lint inspected ${markdown.length} Markdown files.`);
}

async function index(files) {
  const map = join(vault, 'Harita.md');
  if (!existsSync(map)) errors.push('Vault map is missing.');
  const markdownCount = files.filter((file) => extname(file).toLowerCase() === '.md').length;
  console.log(`Vault index: ${markdownCount} Markdown files; canonical map present.`);
}

async function assets(files) {
  const assetFiles = files.filter((file) => assetExtensions.has(extname(file).toLowerCase()));
  for (const file of assetFiles) {
    if ((await stat(file)).size === 0) errors.push(`${display(file)}: empty asset file`);
  }
  console.log(`Asset check inspected ${assetFiles.length} visual files.`);
}

function gitLines(args) {
  const output = execFileSync('git', ['-c', 'core.quotepath=false', ...args], { cwd: root, encoding: 'utf8' });
  return output.split(/\r?\n/).filter(Boolean).map((line) => line.replaceAll('\\', '/'));
}

function isLocalPath(path) {
  return localPrefixes.some((prefix) => path === prefix || path.startsWith(prefix));
}

function isVaultBranchPath(path) {
  return vaultBranchFiles.includes(path) || isLocalPath(path);
}

function currentBranch() {
  return gitLines(['symbolic-ref', '--quiet', '--short', 'HEAD'])[0] ?? 'HEAD';
}

async function prSafety() {
  const tracked = gitLines(['ls-files']);
  const staged = gitLines(['diff', '--cached', '--name-only', '--diff-filter=ACMR']);
  const branch = currentBranch();

  if (branch === vaultBranch) {
    for (const path of tracked.filter((path) => !isVaultBranchPath(path))) {
      errors.push(`${path}: product file is not allowed on ${vaultBranch}`);
    }
    for (const path of staged.filter((path) => !isVaultBranchPath(path))) {
      errors.push(`${path}: staged product file is not allowed on ${vaultBranch}`);
    }
  } else {
    for (const path of tracked.filter(isLocalPath)) errors.push(`${path}: local vault file is tracked`);
    for (const path of staged.filter(isLocalPath)) errors.push(`${path}: local vault file is staged`);
  }

  console.log(`PR safety checked ${tracked.length} tracked and ${staged.length} staged paths on ${branch}.`);
}

async function prePush() {
  await prSafety();
  process.stdin.setEncoding('utf8');
  let input = '';
  for await (const chunk of process.stdin) input += chunk;

  for (const line of input.split(/\r?\n/).filter(Boolean)) {
    const [localRef, localSha, remoteRef] = line.trim().split(/\s+/);
    if (!localRef || !localSha || !remoteRef || /^0+$/.test(localSha)) continue;

    const tree = gitLines(['ls-tree', '-r', '--name-only', localSha]);
    const containsVault = tree.some(isLocalPath);

    if (containsVault && remoteRef !== vaultRemoteRef) {
      errors.push(`${localRef}: vault content may only be pushed to ${vaultRemoteRef}, not ${remoteRef}`);
    }
    if (remoteRef === vaultRemoteRef) {
      for (const path of tree.filter((path) => !isVaultBranchPath(path))) {
        errors.push(`${path}: product file may not be pushed to ${vaultRemoteRef}`);
      }
    }
  }

  console.log(`Pre-push policy checked; vault destination is restricted to ${vaultRemoteRef}.`);
}

async function newAdr(title) {
  if (!title?.trim()) {
    console.error('Usage: node .local-tools/vault.mjs new-adr "Decision title"');
    process.exit(2);
  }
  const directory = join(vault, 'Kararlar');
  await mkdir(directory, { recursive: true });
  const names = await readdir(directory);
  const numbers = names
    .map((name) => /^ADR-(\d+)/.exec(name)?.[1])
    .filter(Boolean)
    .map(Number);
  const next = String((numbers.length ? Math.max(...numbers) : 0) + 1).padStart(3, '0');
  const safeTitle = title.replace(/[<>:"/\\|?*]/g, '-').trim();
  const path = join(directory, `ADR-${next} - ${safeTitle}.md`);
  const today = new Date().toISOString().slice(0, 10);
  const content = `---\ntur: adr\nalan: kararlar\nguncelleme: ${today}\nozet: "${safeTitle}"\ndurum: onerilen\n---\n# ADR-${next}: ${safeTitle}\n\n## Bağlam\n\n## Karar\n\n## Seçenekler\n\n## Sonuçlar\n\n## Doğrulama\n`;
  await writeFile(path, content, { flag: 'wx' });
  console.log(display(path));
}

if (!existsSync(vault)) {
  console.error('Vault root is missing.');
  process.exit(1);
}

if (mode === 'new-adr') {
  await newAdr(process.argv.slice(3).join(' '));
  process.exit(0);
}

const files = await walk(vault);
if (mode === 'index') await index(files);
else if (mode === 'lint') await lint(files);
else if (mode === 'assets') await assets(files);
else if (mode === 'pr-safety') await prSafety();
else if (mode === 'pre-push') await prePush();
else if (mode === 'check') {
  await index(files);
  await lint(files);
  await assets(files);
  await prSafety();
} else {
  console.error(`Unknown vault command: ${mode}`);
  process.exit(2);
}

if (errors.length > 0) {
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log(`Vault ${mode} passed.`);
