# $language = "python"
# $interface = "1.0"

# This automatically generated script may need to be
# edited in order to work correctly.

def Main():
    crt.Screen.Synchronous = True
    crt.Screen.Send("sh int description | match" + chr(9) + ' "vid|VID|stream|Stream|Streami|dvm|hdv|cdv|qpsk|_QPSK|QPSK|ois|sgt|sva|svp|VOB|vas|vdc|vds|vdx|vns|nsg|hvd|HVD|RFGW|apx|apex|STRM|str|TYPE=VID|VIDEO|SDV|sdv|NSG|XOD|DMM|VideoEdg|OUTPUT|DCM|OWNER=VIDEO|MGMT|l3mmt|Video_|Video-|DAC|Apex|,ARP|ARPD-MGMT|chtrav|l3vod|Monitori|Encoder|sen|,OM0|MGMT-OM|GMT-|qmm|VLS-|-VLS|VideoPublic| -qmm|l2adv|chrtav|chrtrc|,netg|TRK|DNCS|monitori|HED:|UMG|=PEER|M_REACH|3K" '+ chr(13))
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
