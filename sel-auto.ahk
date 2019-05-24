#SingleInstance, force
SetTitleMatchMode, 2

if (!WinExist("Sublime")){
	Run subl 
	WinWait, Sublime,,
	WinMinimize, Sublime
}
if (!WinExist("Sel")){
	Run subl D:\1.Manoj\4.Study\4.Codes\99.Z\Sel,
	WinWait, (Sel),,
ControlSend, ahk_parent,^p,(Sel)
Sleep, 1000
ControlSend, ahk_parent,l4l{Enter} ,(Sel)
}
	WinActivate,  (Sel)
; ControlSend, ahk_parent,{ppl4lCtrl Up}p{Ctrl Down} ,(Sel)
Sleep, 1000
ControlSend, ahk_parent,{F7} ,(Sel)
	WinMinimize, (Sel)
