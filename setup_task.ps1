<# 
Registers a Windows Scheduled Task that starts the automation at user logon.
Run this PowerShell as Administrator.
#>
param(
  [string]$PythonPath = "C:\Python311\python.exe"
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$WorkDir = Join-Path $ScriptDir "teams_obs_automation"
$ScriptPath = Join-Path $WorkDir "automate.py"

if (-Not (Test-Path $ScriptPath)) {
  Write-Error "Could not find automate.py at $ScriptPath"
  exit 1
}

$Action = New-ScheduledTaskAction -Execute $PythonPath -Argument "`"$ScriptPath`"" -WorkingDirectory $WorkDir
$Trigger = New-ScheduledTaskTrigger -AtLogOn
$Principal = New-ScheduledTaskPrincipal -UserId $env:UserName -LogonType InteractiveToken
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries

Register-ScheduledTask -TaskName "TeamsOBS_Automation" -Action $Action -Trigger $Trigger -Principal $Principal -Settings $Settings -Force
Write-Output "Task 'TeamsOBS_Automation' registered. It will run at user logon."
