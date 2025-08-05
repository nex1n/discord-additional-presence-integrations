$venvPath = ".\venv\Scripts\Activate.ps1"

function Start-PythonJob($scriptPath, $jobName) {
    Write-Host "Starting $jobName..."
    Start-Job -ScriptBlock {
        param($venvPath, $scriptPath)
        & $venvPath
        python $scriptPath
    } -ArgumentList $venvPath, $scriptPath -Name $jobName
}

$serverJob = Start-PythonJob -scriptPath "server.py" -jobName "ServerJob"
$senderJob = Start-PythonJob -scriptPath "sender.py" -jobName "SenderJob"

Write-Host "Jobs started. Press any key to stop..."
$x = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

Write-Host "Stopping jobs..."

Stop-Job -Id $serverJob.Id
Stop-Job -Id $senderJob.Id

Start-Sleep -Seconds 2

$serverJobState = (Get-Job -Id $serverJob.Id).State
$senderJobState = (Get-Job -Id $senderJob.Id).State

if ($serverJobState -eq "Running" -or $senderJobState -eq "Running") {
    Write-Host "Jobs still running, killing all python processes..."
    Get-Process -Name python -ErrorAction SilentlyContinue | Stop-Process -Force
    Start-Sleep -Seconds 2
}

Remove-Job -Id $serverJob.Id -ErrorAction SilentlyContinue
Remove-Job -Id $senderJob.Id -ErrorAction SilentlyContinue

Write-Host "Jobs stopped and removed."
