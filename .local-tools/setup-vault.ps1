$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$ignoreFile = Join-Path $repoRoot '.better-payment-local-ignore'

git -C $repoRoot config --local core.excludesFile $ignoreFile
if ($LASTEXITCODE -ne 0) { throw 'Could not configure the local Git excludes file.' }
git -C $repoRoot config --local core.hooksPath .local-githooks
if ($LASTEXITCODE -ne 0) { throw 'Could not configure the local Git hooks path.' }

Write-Output 'Local vault ignore file configured.'
Write-Output 'Local Git hooks configured: .local-githooks'
Write-Output 'Vault commits are allowed only on personal/vault; all PR branches remain blocked.'
node (Join-Path $PSScriptRoot 'vault.mjs') check
if ($LASTEXITCODE -ne 0) { throw 'Vault validation failed.' }
