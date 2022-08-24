def Main():
    crt.Screen.Synchronous = True
    crt.Screen.Send("show ver | no-more"  + chr(13))
    crt.Screen.WaitForString(">")
    crt.Screen.Send("show conf | match OSPF | no-more"  + chr(13))
    crt.Screen.WaitForString(">")
    crt.Screen.Send("show conf | match ISIS |  no-more" + chr(13))
    crt.Screen.WaitForString(">")
    crt.Screen.Send("show confi |  match OSPF3 |  no-more" + chr(13))
    crt.Screen.WaitForString(">")
    crt.Screen.Send("show confi |  match BGP | no-more"  + chr(13))
    crt.Screen.WaitForString(">")
    crt.Screen.Send( " show int desc | match up | except down | no-more" + chr(13))
    crt.Screen.WaitForString(">")
    crt.Screen.Send("show bgp summary | no-more" + chr(13))
        
    
Main()
