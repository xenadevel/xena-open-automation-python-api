import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from typing import Coroutine
from xoa_driver.functions.config_cli_convert import CLIConverter  # noqa: E402


@pytest.mark.asyncio
async def test_config_cli() -> None:
    c_commands = """C_LOGON "xena"
C_OWNER "Bob"
C_OWNER ?
C_KEEPALIVE ?
C_TIMEOUT 100
C_TIMEOUT ?
C_RESERVATION RELEASE
C_RESERVATION ?
C_RESERVEDBY ?
C_LOGOFF
C_DOWN -1480937026 RESTART
C_CAPABILITIES ?
C_MODEL ?
C_SERIALNO ?
C_VERSIONNO ?
C_PORTCOUNTS ?
C_PORTERRORS ?
C_REMOTEPORTCOUNTS ?
C_BUILDSTRING ?
C_NAME "L23 Live Demo"
C_NAME ?
C_COMMENT "this a comment"
C_COMMENT ?
C_PASSWORD "abcd"
C_PASSWORD ?
C_IPADDRESS 192.168.1.100 255.255.255.0 192.168.1.1
C_IPADDRESS ?
C_DHCP OFF
C_DHCP ?
C_MACADDRESS ?
C_HOSTNAME "xena-123456"
C_HOSTNAME ?
C_FLASH OFF
C_FLASH ?
C_DEBUGLOGS ?
C_TEMPERATURE ?
C_RESTPORT 1
C_RESTPORT ?
C_RESTENABLE OFF
C_RESTENABLE ?
C_RESTCONTROL START
C_RESTSTATUS ?
C_WATCHDOG 1
C_WATCHDOG ?
C_INDICES ?
C_STATSESSION [0] ?
# C_TKLICFILE "a string"
C_TKLICFILE ?
C_TKLICSTATE ?
# C_FILESTART 0x01 0x01 0x01020304 0x444 0xedfe4432 "filename"
C_FILEDATA 1 0x1E2E3E4E5E1E2E3E4E5E1E2E3E4E5E1E2E3E4E5E1E2E3E4E5E
C_FILEFINISH
C_TRAFFIC OFF 0 0 0 1
C_VERSIONNO_MINOR ?
C_START 0 0 0 1
C_STOP 0 0 0 1
C_MULTIUSER ?
C_SCRIPT "C_MODEL ?"
C_TKSTATUS ?
C_TKSVCSTATE STOP
C_TKSVCSTATE ?
C_TKGPSSTATE ?
C_TIME ?
C_TRAFFICSYNC OFF 2147483647 0 0 0 1
C_TRAFFICSYNC ?
C_TKSTATUSEXT ?
"""

    m_commands = """0 M_RESERVATION RELEASE
0 M_RESERVATION ? 
0 M_RESERVEDBY ?
0 M_MODEL ?
0 M_SERIALNO ?
0 M_VERSIONNO ?
0 M_STATUS ?
0 M_PORTCOUNT ?
0 M_UPGRADE "image.name"
0 M_UPGRADEPROGRESS ?
0 M_TIMESYNC CHASSIS
0 M_TIMESYNC ?
0 M_CFPTYPE ?
0 M_COMMENT "comment"
0 M_TIMEADJUSTMENT 1
0 M_CAPABILITIES ?
0 M_MEDIASUPPORT ?
0 M_FPGAREIMAGE
0 M_MULTIUSER ?
0 M_CFPCONFIGEXT ?
0 M_CLOCKPPB ?
0 M_SMAINPUT NOTUSED
0 M_SMASTATUS ?
0 M_NAME ?
0 M_REVISION ?
0 M_MEDIA CFP4
0 M_MEDIA ?
0 M_CLOCKSYNCSTATUS ?
0 M_LICENSE_DEMO_INFO ?
0 M_LICENSE_MAINTENANCE_INFO ?
0 M_LICENSE_CWB_DETECTED ?
0 M_LICENSE_UPDATE
0 M_LICENSE_UPDATE_STATUS ?
0 M_LICENSE_LIST_BSON ?
0 M_LICENSE_ONLINE OFFLINE
0 M_TXCLOCKSOURCE_NEW MODULELOCALCLOCK
0 M_TXCLOCKSTATUS_NEW ?
0 M_TXCLOCKFILTER_NEW BW103HZ
0 M_CLOCKPPBSWEEP TRIANGLE 10000 1000000 100000 0
0 M_CLOCKSWEEPSTATUS ?
"""

    p_commands = """
0/1 P_RESERVATION RELEASE
0/1 P_RESERVATION ?
0/1 P_RESERVEDBY ?
0/1 P_RESET
0/1 P_CAPABILITIES ?
0/1 P_INTERFACE ?
0/1 P_SPEEDSELECTION AUTO
0/1 P_SPEEDSELECTION ?
0/1 P_SPEED ?
0/1 P_RECEIVESYNC ?
0/1 P_COMMENT "This is a comment"
0/1 P_COMMENT ?
0/1 P_SPEEDREDUCTION 1
0/1 P_SPEEDREDUCTION ?
0/1 P_INTERFRAMEGAP 1
0/1 P_INTERFRAMEGAP ?
0/1 P_MACADDRESS 0x1234FFFFE1E2
0/1 P_MACADDRESS ?
0/1 P_IPADDRESS 192.168.1.100 255.255.255.0 192.168.1.1 255.255.255.255
0/1 P_IPADDRESS ?
0/1 P_ARPREPLY OFF
0/1 P_ARPREPLY ?
0/1 P_PINGREPLY OFF
0/1 P_PINGREPLY ?
0/1 P_PAUSE OFF
0/1 P_PAUSE ?
0/1 P_RANDOMSEED 1
0/1 P_RANDOMSEED ?
0/1 P_LOOPBACK NONE
0/1 P_LOOPBACK ?
0/1 P_FLASH OFF
0/1 P_FLASH ?
0/1 P_TRAFFIC STOP
0/1 P_TRAFFIC ?
0/1 P_CAPTURE STOP
0/1 P_CAPTURE ?
0/1 P_XMITONE 0x04f4bc19a2a104f4bc19a2a0080045000032000000007fff12b70a0a0a010a0a0a0222232425262728292a2b000000c560b75a001e2280006a7e7f95b0da09c5
0/1 P_LATENCYOFFSET 1
0/1 P_LATENCYOFFSET ? 
0/1 P_LATENCYMODE LAST2LAST
0/1 P_LATENCYMODE ?
0/1 P_AUTOTRAIN 1
0/1 P_AUTOTRAIN ?
0/1 P_UAT_MODE OFF 1
0/1 P_UAT_MODE ?
0/1 P_UAT_FLR 1
0/1 P_UAT_FLR ?
0/1 P_MIXWEIGHTS 0 0 0 0 57 3 5 1 2 5 1 4 4 18 0 0
0/1 P_MIXWEIGHTS ?
0/1 P_MDIXMODE AUTO
0/1 P_MDIXMODE ?
0/1 P_TRAFFICERR ?
0/1 P_GAPMONITOR 1 1
0/1 P_GAPMONITOR ?
0/1 P_CHECKSUM 1
0/1 P_CHECKSUM ?
0/1 P_STATUS ?
0/1 P_AUTONEGSELECTION OFF
0/1 P_AUTONEGSELECTION ?
0/1 P_MIXLENGTH [0] 1
0/1 P_MIXLENGTH [0] ?
0/1 P_ARPRXTABLE 0x0A0A0A0A0018011122334455660B0B0B0B001801998877665544
0/1 P_ARPRXTABLE ?
0/1 P_NDPRXTABLE 0x00000000000000000000000000000123008001112233445566
0/1 P_NDPRXTABLE ?
0/1 P_MULTICAST 192.168.1.100 OFF 1
0/1 P_MULTICAST ?
0/1 P_MULTICASTEXT 192.168.1.100 OFF 1 IGMPV2
0/1 P_MULTICASTEXT ?
0/1 P_MCSRCLIST 192.168.1.100
0/1 P_MCSRCLIST ?
0/1 P_TXMODE NORMAL
0/1 P_TXMODE ?
0/1 P_MULTICASTHDR 1 NOHDR 1 1 OFF
0/1 P_MULTICASTHDR ?
0/1 P_RATEFRACTION 1
0/1 P_RATEFRACTION ?
0/1 P_RATEPPS 1
0/1 P_RATEPPS ?
0/1 P_RATEL2BPS 1
0/1 P_RATEL2BPS ?
0/1 P_PAYLOADMODE NORMAL
0/1 P_PAYLOADMODE ?
0/1 P_BRRMODE SLAVE
0/1 P_BRRMODE ?
0/1 P_TXENABLE OFF
0/1 P_TXENABLE ?
0/1 P_MAXHEADERLENGTH 1
0/1 P_MAXHEADERLENGTH ?
0/1 P_TXTIMELIMIT 1
0/1 P_TXTIMELIMIT ?
0/1 P_TXTIME ?
0/1 P_XMITONETIME ?
0/1 P_IPV6ADDRESS ::1 ::1 1 1
0/1 P_IPV6ADDRESS ?
0/1 P_ARPV6REPLY OFF
0/1 P_ARPV6REPLY ?
0/1 P_PINGV6REPLY OFF
0/1 P_PINGV6REPLY ?
0/1 P_ERRORS ?
0/1 P_TXPREPARE
0/1 P_TXDELAY ?
0/1 P_LPENABLE OFF
0/1 P_LPENABLE ?
0/1 P_LPTXMODE OFF
0/1 P_LPTXMODE ?
0/1 P_LPSTATUS ?
0/1 P_LPPARTNERAUTONEG ?
0/1 P_LPSNRMARGIN ?
0/1 P_LPRXPOWER ?
0/1 P_FAULTSIGNALING NORMAL
0/1 P_FAULTSIGNALING ?
0/1 P_FAULTSTATUS ?
0/1 P_TPLDMODE NORMAL
0/1 P_TPLDMODE ?
0/1 P_LPSUPPORT ?
0/1 P_TXPACKETLIMIT 1 
0/1 P_TXPACKETLIMIT ?
0/1 P_TCVRSTATUS ?
0/1 P_DYNAMIC OFF
0/1 P_DYNAMIC ?
0/1 P_PFCENABLE OFF OFF OFF OFF OFF OFF OFF OFF
0/1 P_PFCENABLE ?
0/1 P_TXBURSTPERIOD 1
0/1 P_TXBURSTPERIOD ?
0/1 P_TXRUNTLENGTH 1
0/1 P_TXRUNTLENGTH ?
0/1 P_RXRUNTLENGTH 1
0/1 P_RXRUNTLENGTH ?
0/1 P_RXRUNTLEN_ERRS ?
0/1 P_TXPREAMBLE_REMOVE OFF
0/1 P_TXPREAMBLE_REMOVE ?
0/1 P_RXPREAMBLE_INSERT OFF
0/1 P_RXPREAMBLE_INSERT ?
0/1 P_SPEEDS_SUPPORTED ?    
"""
    pc_commands = """
0/1 PC_TRIGGER ON 1 FULL 1
0/1 PC_TRIGGER ?
0/1 PC_KEEP ALL 1 1
0/1 PC_KEEP ?
0/1 PC_STATS ?
0/1 PC_EXTRA [0] ?
0/1 PC_PACKET [0] ?
"""
    pd_commands = """
0/1 PD_INDICES 0 1
0/1 PD_INDICES ?
0/1 PD_CREATE [0]
0/1 PD_DELETE [0]
0/1 PD_ENABLE [0] OFF
0/1 PD_ENABLE [0] ?
0/1 PD_SOURCE [0] TXIFG ALL 1
0/1 PD_SOURCE [0] ?
0/1 PD_RANGE [0] 1 1 1
0/1 PD_RANGE [0] ?
0/1 PD_SAMPLES [0] ?    
"""
    pf_commands = """
0/1 PF_INDICES 0 1
0/1 PF_INDICES ?
0/1 PF_CREATE [0]
0/1 PF_DELETE [0]
0/1 PF_ENABLE [0] OFF
0/1 PF_ENABLE [0] ?
0/1 PF_COMMENT [0] 'this is a comment'
0/1 PF_COMMENT [0] ?
0/1 PF_CONDITION [0] 1 1 1 1 1 1
0/1 PF_CONDITION [0] ?
0/1 PF_STRING [0] "a string"
0/1 PF_STRING [0] ?    
"""
    pl_commands = """
0/1 PL_INDICES 0 1
0/1 PL_INDICES ?
0/1 PL_CREATE [0]
0/1 PL_DELETE [0]
0/1 PL_LENGTH [0] AT_MOST 1
0/1 PL_LENGTH [0] ?   
"""
    pm_commands = """
0/1 PM_INDICES 0 1
0/1 PM_INDICES ?
0/1 PM_CREATE [0]
0/1 PM_DELETE [0]
0/1 PM_PROTOCOL [0] ETHERNET VLAN IP -4
0/1 PM_PROTOCOL [0] ?
0/1 PM_POSITION [0] 1
0/1 PM_POSITION [0] ?
0/1 PM_MATCH [0] 0xFF00000000000000 0x0000000000000000
0/1 PM_MATCH [0] ?    
"""
    pp_commands = """
0/1 PP_ALARMS_ERRORS ?
0/1 PP_TXLANECONFIG [0] 1 1
0/1 PP_TXLANECONFIG [0] ?
0/1 PP_TXLANEINJECT [0] HEADERERROR
0/1 PP_TXPRBSCONFIG [0] 1 PRBSOFF ERRORSOFF
0/1 PP_TXPRBSCONFIG [0] ?
0/1 PP_TXERRORRATE 1
0/1 PP_TXERRORRATE ?
0/1 PP_TXINJECTONE
0/1 PP_RXTOTALSTATS ?
0/1 PP_RXFECSTATS ?
0/1 PP_LINKFLAP_PARAMS 1 1 1
0/1 PP_LINKFLAP_PARAMS ?
0/1 PP_LINKFLAP_ENABLE OFF
0/1 PP_LINKFLAP_ENABLE ?
0/1 PP_PMAERRPUL_PARAMS 1 1 1 1 1
0/1 PP_PMAERRPUL_PARAMS ?
0/1 PP_RXLANELOCK [0] ?
0/1 PP_RXLANESTATUS [0] ?
0/1 PP_RXLANEERRORS [0] ?
0/1 PP_RXPRBSSTATUS [0] ?
0/1 PP_RXCLEAR
0/1 PP_RXLASERPOWER ?
0/1 PP_TXLASERPOWER ?
0/1 PP_PMAERRPUL_ENABLE OFF
0/1 PP_PMAERRPUL_ENABLE ?
0/1 PP_EYEMEASURE [0] STOP 0
0/1 PP_EYEMEASURE [0] ?
0/1 PP_EYERESOLUTION [0] 1 1
0/1 PP_EYERESOLUTION [0] ?
0/1 PP_EYEREAD [0, 0] ?
0/1 PP_EYEINFO [0] ? 
0/1 PP_PHYTXEQ [0] 0 128 0 0 0 0 4 2
0/1 PP_PHYTXEQ [0] ?
0/1 PP_PHYRETUNE [0] 1
0/1 PP_PHYAUTOTUNE [0] OFF
0/1 PP_PHYAUTOTUNE [0] ?
0/1 PP_EYEBER [0] ?
0/1 PP_PHYAUTONEG OFF 1 1 1 1
0/1 PP_PHYAUTONEG ?
0/1 PP_TXPRBSTYPE CAUI_VIRTUAL PRBS7 NON_INVERTED
0/1 PP_TXPRBSTYPE ?
0/1 PP_RXPRBSTYPE CAUI_VIRTUAL PRBS7 NON_INVERTED ACCUMULATIVE
0/1 PP_RXPRBSTYPE ?
0/1 PP_FECMODE OFF
0/1 PP_FECMODE ?
0/1 PP_EYEDWELLBITS [0] 1 1
0/1 PP_EYEDWELLBITS [0] ?
0/1 PP_PHYSIGNALSTATUS ?
0/1 PP_PRBSTYPE CAUI_VIRTUAL PRBS7 NON_INVERTED ACCUMULATIVE
0/1 PP_PRBSTYPE ?
0/1 PP_PHYSETTINGS OFF OFF OFF OFF
0/1 PP_PHYSETTINGS ?
0/1 PP_PHYRXEQ [0] 1 1 1
0/1 PP_PHYRXEQ [0] ?
0/1 PP_AUTONEG ANEG_OFF DEFAULT_TECH_MODE DEFAULT_FEC DEFAULT_FEC NO_PAUSE
0/1 PP_AUTONEG ?
0/1 PP_AUTONEGSTATUS ?
0/1 PP_LINKTRAIN AUTO P16K_FRAME NO_INIT NRZ_NO_PRESET DEFAULT_TIMEOUT
0/1 PP_LINKTRAIN ?
0/1 PP_LINKTRAINSTATUS [0] ?    
"""
    ps_commands = """
0/1 PS_INDICES 0 1
0/1 PS_INDICES ?
0/1 PS_CREATE [0]
0/1 PS_DELETE [0]
0/1 PS_ENABLE [0] OFF
0/1 PS_ENABLE [0] ?
0/1 PS_PACKETLIMIT [0] 1
0/1 PS_PACKETLIMIT [0] ?
0/1 PS_COMMENT [0] "this is a comment"
0/1 PS_COMMENT [0] ?
0/1 PS_TPLDID [0] 1
0/1 PS_TPLDID [0] ?
0/1 PS_INSERTFCS [0] OFF
0/1 PS_INSERTFCS [0] ?
0/1 PS_ARPREQUEST [0] ?
0/1 PS_PINGREQUEST [0] ?
0/1 PS_MODIFIEREXTRANGE [0, 0] 1 1 1
0/1 PS_MODIFIEREXTRANGE [0, 0] ?
0/1 PS_MODIFIERRANGE [0, 0] 1 1 1
0/1 PS_MODIFIERRANGE [0, 0] ?
0/1 PS_RATEFRACTION [0] 1
0/1 PS_RATEFRACTION [0] ?
0/1 PS_RATEPPS [0] 1
0/1 PS_RATEPPS [0] ?
0/1 PS_RATEL2BPS [0] 1
0/1 PS_RATEL2BPS [0] ?
0/1 PS_BURST [0] 1 1
0/1 PS_BURST [0] ?
0/1 PS_PACKETHEADER [0] 0xAAAAAAAAAAAA04F4BC9DE7008100000A08004500002A000000007FFF3AD60000000000000000
0/1 PS_PACKETHEADER [0] ?
0/1 PS_HEADERPROTOCOL [0] ETHERNET VLAN IP -4
0/1 PS_HEADERPROTOCOL [0] ?
0/1 PS_MODIFIERCOUNT [0] 1
0/1 PS_MODIFIERCOUNT [0] ?
0/1 PS_MODIFIER [0, 0] 14 0xFF INC 1
0/1 PS_MODIFIER [0, 0] ?
0/1 PS_AUTOADJUST [0]
0/1 PS_PACKETLENGTH [0] FIXED 1 1
0/1 PS_PACKETLENGTH [0] ?
0/1 PS_PAYLOAD [0] PATTERN 0x000102030405060708090A0B0C0D0E0F
0/1 PS_PAYLOAD [0] ?
0/1 PS_IPV4GATEWAY [0] 192.168.1.1
0/1 PS_IPV4GATEWAY [0] ?
0/1 PS_IPV6GATEWAY [0] ::1
0/1 PS_IPV6GATEWAY [0] ?
0/1 PS_BURSTGAP [0] 1 1
0/1 PS_BURSTGAP [0] ?
0/1 PS_INJECTFCSERR [0]
0/1 PS_INJECTSEQERR [0]
0/1 PS_INJECTMISERR [0]
0/1 PS_INJECTPLDERR [0]
0/1 PS_INJECTTPLDERR [0]
0/1 PS_MODIFIEREXT [0, 0] 14 0xFFFF INC 1 
0/1 PS_MODIFIEREXT [0, 0] ?
0/1 PS_CDFCOUNT [0] 1 
0/1 PS_CDFCOUNT [0] ?
0/1 PS_CDFDATA [0, 0] 0x3333333333333333
0/1 PS_CDFDATA [0, 0] ?
0/1 PS_EXTPAYLOAD [0] 0x123AA123BB123CC123AA123BB123CC123AA123BB123CC
0/1 PS_EXTPAYLOAD [0] ?
0/1 PS_PFCPRIORITY [0] VLAN_PCP
0/1 PS_PFCPRIORITY [0] ?
"""
    pt_commands = """
0/1 PT_TOTAL ?
0/1 PT_TOTALEXT ?
0/1 PT_NOTPLD ?
0/1 PT_NOTPLDEXT ?
0/1 PT_STREAM [0] ?
0/1 PT_STREAMEXT [0] ?
0/1 PT_CLEAR
0/1 PT_EXTRA ?
"""
    pr_commands = """    
0/1 PR_TPLDJITTER [0] ?
0/1 PR_TOTAL ?
0/1 PR_TOTALEXT ?
0/1 PR_NOTPLD ?
0/1 PR_NOTPLDEXT ?
0/1 PR_EXTRA ?
0/1 PR_TPLDS ?
0/1 PR_TPLDTRAFFIC [0] ?
0/1 PR_TPLDTRAFFICEXT [0] ?
0/1 PR_TPLDERRORS [0] ?
0/1 PR_TPLDLATENCY [0] ?
0/1 PR_FILTER [0] ?
0/1 PR_FILTEREXT [0] ?
0/1 PR_CLEAR
0/1 PR_CALIBRATE
0/1 PR_PFCSTATS ?
0/1 PR_UAT_STATUS ?
0/1 PR_UAT_TIME ?    
"""
    px_commands = """
0/1 PX_TEMPERATURE ?
0/1 PX_MII [0x1400] 0x0011
0/1 PX_MII [0] 0x0011
0/1 PX_MII [0x00] ?
0/1 PX_MII [0] ?
0/1 PX_RW [0x00,0x56] 0x0000000F
0/1 PX_RW [0,86] 0x0000000F
0/1 PX_RW [0x00,0x56] ?
0/1 PX_RW [0,86] ?
0/1 PX_RW_SEQ [0x00,0x14,0x0A] 0x00001111222200001111
0/1 PX_RW_SEQ [0,20,10] 0x00001111222200001111
0/1 PX_RW_SEQ [0x00,0x14,0x0A] ?
0/1 PX_RW_SEQ [0,20,10] ?    
"""
    pl1_commands = """
0/1 PL1_AUTONEGINFO [0x00] ?
0/0 PL1_LINKTRAININFO [0, 0] ?
0/0 PL1_LOG [0x00, 1] ?
0/0 PL1_CFG_TMP [0x00, 1] ON
0/0 PL1_CFG_TMP [0x00, 1] ?
0/0 PL1_LINKTRAIN_CMD [0x00] CMD_INC PRE1
0/0 PL1_LINKTRAIN_CMD [0x00] ?    
"""
    m4_commands = """
0 M4_SYSTEMID ?
0 M4_VERSIONNO ?
0 M4_SYSTEM_STATUS ?
0 M4_COMPATIBLE_CLIENT_VERSION ?
0 M4_TIME ?
0 M4_SYSTEM_TIME 2020 4 19 7 25 00
0 M4_SYSTEM_TIME ?
0 M4_MEM_INFO ?
0 M4_CAPTURE_SIZE FULL
0 M4_CAPTURE_SIZE ?
0 M4_LICENSE_INFO ?
0 M4_REPLAY_PARSE_START 'A String'
0 M4_REPLAY_PARSE_STOP
0 M4_REPLAY_PARSE_STATE ?
0 M4_REPLAY_PARSER_PARAMS 1
0 M4_REPLAY_PARSER_PARAMS ?
0 M4_REPLAY_FILE_LIST_BSON ?
0 M4_REPLAY_FILE_LIST ?
0 M4_CAPTURE_FILE_LIST_BSON ?
0 M4_CAPTURE_FILE_LIST ?
0 M4_REPLAY_FILE_DELETE 'A String'
0 M4_CAPTURE_FILE_DELETE 'A String'
0 M4_TLS_CIPHER_SUITES ?
"""
    m4e_commands = """
0 M4E_MODE SIMPLE
0 M4E_MODE ?
0 M4E_RESERVE 0x00000000000000ff
0 M4E_RESERVE ?    
"""
    p4_commands = """
0/1 P4_TRAFFIC OFF
0/1 P4_STATE ?
0/1 P4_CAPABILITIES ?
0/1 P4_STATE_STATUS ?
0/1 P4_VLAN_OFFLOAD OFF
0/1 P4_VLAN_OFFLOAD ?
0/1 P4_ARP_CONFIG 100 100 32
0/1 P4_ARP_CONFIG ?
0/1 P4_NDP_CONFIG 100 100 32
0/1 P4_NDP_CONFIG ?
0/1 P4_CAPTURE OFF
0/1 P4_CAPTURE ?
0/1 P4_CAPTURE_GET_FIRST ?
0/1 P4_CAPTURE_GET_NEXT ?
0/1 P4_ETH_TX_COUNTERS ?
0/1 P4_ETH_RX_COUNTERS ?
0/1 P4_PORT_TX_COUNTERS ?
0/1 P4_PORT_RX_COUNTERS ?
0/1 P4_PORT_COUNTERS ?
0/1 P4_TX_PACKET_SIZE ?
0/1 P4_RX_PACKET_SIZE ?
0/1 P4_TX_MTU ?
0/1 P4_RX_MTU ? 
0/1 P4_IPV4_RX_COUNTERS ?
0/1 P4_IPV4_TX_COUNTERS ?
0/1 P4_IPV4_COUNTERS ?
0/1 P4_IPV6_RX_COUNTERS ?
0/1 P4_IPV6_TX_COUNTERS ?
0/1 P4_IPV6_COUNTERS ?
0/1 P4_ARP_RX_COUNTERS ?
0/1 P4_ARP_TX_COUNTERS ?
0/1 P4_ARP_COUNTERS ?
0/1 P4_NDP_RX_COUNTERS ?
0/1 P4_NDP_TX_COUNTERS ?
0/1 P4_NDP_COUNTERS ?
0/1 P4_ICMP_RX_COUNTERS ?
0/1 P4_ICMP_TX_COUNTERS ?
0/1 P4_ICMP_COUNTERS ?
0/1 P4_TCP_RX_COUNTERS ?
0/1 P4_TCP_TX_COUNTERS ?
0/1 P4_TCP_COUNTERS ?
0/1 P4_UDP_RX_COUNTERS ?
0/1 P4_UDP_TX_COUNTERS ?
0/1 P4_UDP_COUNTERS ?
0/1 P4_CLEAR_COUNTERS
0/1 P4_ETH_COUNTERS ?
0/1 P4_CLEAR
0/1 P4_SPEEDSELECTION AUTO
0/1 P4_SPEEDSELECTION ?
0/1 P4_MAX_PACKET_RATE AUTOMATIC 1 1
0/1 P4_MAX_PACKET_RATE ?
0/1 P4_PCI_INFO ?
0/1 P4_FW_VER ?
0/1 P4_DEV_NAME ?
0/1 P4_PORT_TYPE ?
0/1 P4_LICENSE_INFO ?
0/1 P4_APTITUDES ?
"""
    p4e_commands = """
1/0 P4E_ASSIGN 0x0000000040001fff
1/0 P4E_ASSIGN ?
1/0 P4E_AVAILABLE ?
1/1 P4E_ALLOCATE 2
1/1 P4E_ALLOCATE ?
1/0 P4E_ALLOCATION_INFO ?   
"""
    p4g_commands = """
0/1 P4G_INDICES 0 1
0/1 P4G_INDICES ?
0/1 P4G_CREATE [0]
0/1 P4G_DELETE [0]
0/1 P4G_ENABLE [0] OFF
0/1 P4G_ENABLE [0] ?
0/1 P4G_COMMENT [0] 'A String'
0/1 P4G_COMMENT [0] ?
0/1 P4G_CLEAR_COUNTERS [0]
0/1 P4G_ROLE [0] CLIENT
0/1 P4G_ROLE [0] ?
0/1 P4G_CLIENT_RANGE [0] 192.168.1.100 1 1 1 1
0/1 P4G_CLIENT_RANGE [0] ?
0/1 P4G_SERVER_RANGE [0] 192.168.1.100 1 1 1
0/1 P4G_SERVER_RANGE [0] ?
0/1 P4G_LP_TIME_SCALE [0] MSECS
0/1 P4G_LP_TIME_SCALE [0] ?
0/1 P4G_LP_SHAPE [0] 1 1 1 1
0/1 P4G_LP_SHAPE [0] ?
0/1 P4G_NAT [0] OFF
0/1 P4G_NAT [0] ?
0/1 P4G_TCP_RTT_VALUE [0] ?
0/1 P4G_TCP_STATE_CURRENT [0] ?
0/1 P4G_TCP_STATE_TOTAL [0] ?
0/1 P4G_TCP_STATE_RATE [0] ?
0/1 P4G_TCP_RX_PAYLOAD_COUNTERS [0] ?
0/1 P4G_TCP_TX_PAYLOAD_COUNTERS [0] ?
0/1 P4G_TCP_RETRANSMIT_COUNTERS [0] ?
0/1 P4G_TCP_ERROR_COUNTERS [0] ?
0/1 P4G_IP_DS_TYPE [0] FIXED
0/1 P4G_IP_DS_TYPE [0] ?
0/1 P4G_IP_DS_VALUE [0] 'A'
0/1 P4G_IP_DS_VALUE [0] ?
0/1 P4G_IP_DS_MASK [0] 'A'
0/1 P4G_IP_DS_MASK [0] ?
0/1 P4G_IP_DS_MINMAX [0] 'A' 'A'
0/1 P4G_IP_DS_MINMAX [0] ?
0/1 P4G_IP_DS_STEP [0] 'A'
0/1 P4G_IP_DS_STEP [0] ?
0/1 P4G_TCP_MSS_TYPE [0] FIXED
0/1 P4G_TCP_MSS_TYPE [0] ?
0/1 P4G_TCP_MSS_MINMAX [0] 1 1
0/1 P4G_TCP_MSS_MINMAX [0] ?
0/1 P4G_TCP_MSS_VALUE [0] 1
0/1 P4G_TCP_MSS_VALUE [0] ?
0/1 P4G_TCP_WINDOW_SIZE [0] 1
0/1 P4G_TCP_WINDOW_SIZE [0] ?
0/1 P4G_TCP_DUP_THRES [0] 1
0/1 P4G_TCP_DUP_THRES [0] ?
0/1 P4G_TCP_SYN_RTO [0] 1 1 1
0/1 P4G_TCP_SYN_RTO [0] ?
0/1 P4G_TCP_RTO [0] STATIC 1 1 1
0/1 P4G_TCP_RTO [0] ?
0/1 P4G_UDP_PACKET_SIZE_TYPE [0] FIXED
0/1 P4G_UDP_PACKET_SIZE_TYPE [0] ?
0/1 P4G_UDP_PACKET_SIZE_MINMAX [0] 1 1
0/1 P4G_UDP_PACKET_SIZE_MINMAX [0] ?
0/1 P4G_UDP_PACKET_SIZE_VALUE [0] 1
0/1 P4G_UDP_PACKET_SIZE_VALUE [0] ?
0/1 P4G_TCP_CONGESTION_MODE [0] NONE
0/1 P4G_TCP_CONGESTION_MODE [0] ?
0/1 P4G_TCP_WINDOW_SCALING [0] NO 1
0/1 P4G_TCP_WINDOW_SCALING [0] ?
0/1 P4G_TCP_RTO_MINMAX [0] 1 1
0/1 P4G_TCP_RTO_MINMAX [0] ?
0/1 P4G_TCP_RTO_PROLONGED_MODE [0] DISABLE 1
0/1 P4G_TCP_RTO_PROLONGED_MODE [0] ?
0/1 P4G_TCP_ICWND_CALC_METHOD [0] RFC5681 1
0/1 P4G_TCP_ICWND_CALC_METHOD [0] ?
0/1 P4G_TCP_ISSTHRESH [0] AUTOMATIC 1
0/1 P4G_TCP_ISSTHRESH [0] ?
0/1 P4G_TCP_ACK_FREQUENCY [0] 1
0/1 P4G_TCP_ACK_FREQUENCY [0] ?
0/1 P4G_TCP_ACK_TIMEOUT [0] 1
0/1 P4G_TCP_ACK_TIMEOUT [0] ?
0/1 P4G_L2_CLIENT_MAC [0] 'A' DONT_EMBED_IP
0/1 P4G_L2_CLIENT_MAC [0] ?
0/1 P4G_L2_SERVER_MAC [0] 'A' DONT_EMBED_IP
0/1 P4G_L2_SERVER_MAC [0] ?
0/1 P4G_L2_USE_ADDRESS_RES [0] NO
0/1 P4G_L2_USE_ADDRESS_RES [0] ?
0/1 P4G_L2_USE_GW [0] NO
0/1 P4G_L2_USE_GW [0] ?
0/1 P4G_L2_GW [0] 192.168.1.100 'A'
0/1 P4G_L2_GW [0] ?
0/1 P4G_L2_IPV6_GW [0] ::1 'A'
0/1 P4G_L2_IPV6_GW [0] ?
0/1 P4G_TEST_APPLICATION [0] NONE
0/1 P4G_TEST_APPLICATION [0] ?
0/1 P4G_RAW_TEST_SCENARIO [0] DOWNLOAD
0/1 P4G_RAW_TEST_SCENARIO [0] ?
0/1 P4G_RAW_PAYLOAD_TYPE [0] FIXED
0/1 P4G_RAW_PAYLOAD_TYPE [0] ?
0/1 P4G_RAW_PAYLOAD_TOTAL_LEN [0] INFINITE 1
0/1 P4G_RAW_PAYLOAD_TOTAL_LEN [0] ?
0/1 P4G_RAW_PAYLOAD [0] 1 1 'A'
0/1 P4G_RAW_PAYLOAD [0] ?
0/1 P4G_RAW_PAYLOAD_REPEAT_LEN [0] 1
0/1 P4G_RAW_PAYLOAD_REPEAT_LEN [0] ?
0/1 P4G_RAW_HAS_DOWNLOAD_REQ [0] NO
0/1 P4G_RAW_HAS_DOWNLOAD_REQ [0] ?
0/1 P4G_RAW_CLOSE_CONN [0] NONE
0/1 P4G_RAW_CLOSE_CONN [0] ?
0/1 P4G_RAW_UTILIZATION [0] 1
0/1 P4G_RAW_UTILIZATION [0] ?
0/1 P4G_RAW_DOWNLOAD_REQUEST [0] 1 'A'
0/1 P4G_RAW_DOWNLOAD_REQUEST [0] ?
0/1 P4G_RAW_TX_DURING_RAMP [0] NO NO
0/1 P4G_RAW_TX_DURING_RAMP [0] ?
0/1 P4G_RAW_TX_TIME_OFFSET [0] 1 1
0/1 P4G_RAW_TX_TIME_OFFSET [0] ?
0/1 P4G_RAW_BURSTY_TX [0] OFF
0/1 P4G_RAW_BURSTY_TX [0] ?
0/1 P4G_RAW_BURSTY_CONF [0] 1 1
0/1 P4G_RAW_BURSTY_CONF [0] ?
0/1 P4G_VLAN_ENABLE [0] OFF
0/1 P4G_VLAN_ENABLE [0] ?
0/1 P4G_VLAN_TCI [0] 'A'
0/1 P4G_VLAN_TCI [0] ?
0/1 P4G_TIME_HIST_CONF [0] 1 1
0/1 P4G_TIME_HIST_CONF [0] ?
0/1 P4G_PAYLOAD_HIST_CONF [0] 1 1
0/1 P4G_PAYLOAD_HIST_CONF [0] ?
0/1 P4G_TRANSACTION_HIST_CONF [0] 1 1
0/1 P4G_TRANSACTION_HIST_CONF [0] ?
0/1 P4G_RAW_RX_PAYLOAD_LEN [0] INFINITE 1
0/1 P4G_RAW_RX_PAYLOAD_LEN [0] ?
0/1 P4G_RAW_REQUEST_REPEAT [0] INFINITE 1
0/1 P4G_RAW_REQUEST_REPEAT [0] ?
0/1 P4G_RAW_CONN_INCARNATION [0] ONCE
0/1 P4G_RAW_CONN_INCARNATION [0] ?
0/1 P4G_RAW_CONN_REPETITIONS [0] INFINITE 1
0/1 P4G_RAW_CONN_REPETITIONS [0] ?
0/1 P4G_RAW_CONN_LIFETIME [0] MSECS 1
0/1 P4G_RAW_CONN_LIFETIME [0] ?
0/1 P4G_IP_VERSION [0] IPV4
0/1 P4G_IP_VERSION [0] ?
0/1 P4G_IPV6_CLIENT_RANGE [0] ::1 1 1 1 1
0/1 P4G_IPV6_CLIENT_RANGE [0] ?
0/1 P4G_IPV6_SERVER_RANGE [0] ::1 1 1 1
0/1 P4G_IPV6_SERVER_RANGE [0] ?
0/1 P4G_IPV6_TRAFFIC_CLASS [0] 'A'
0/1 P4G_IPV6_TRAFFIC_CLASS [0] ?
0/1 P4G_IPV6_FLOW_LABEL [0] 'A'
0/1 P4G_IPV6_FLOW_LABEL [0] ?
0/1 P4G_L4_PROTOCOL [0] TCP
0/1 P4G_L4_PROTOCOL [0] ?
0/1 P4G_TCP_ESTABLISH_HIST [0] ?
0/1 P4G_TCP_CLOSE_HIST [0] ?
0/1 P4G_TCP_RX_TOTAL_BYTES_HIST [0] ?
0/1 P4G_TCP_TX_TOTAL_BYTES_HIST [0] ?
0/1 P4G_TCP_TX_GOOD_BYTES_HIST [0] ?
0/1 P4G_APP_REPLAY_COUNTERS [0] ?
0/1 P4G_APP_TRANSACTION_COUNTERS [0] ?
0/1 P4G_APP_TRANSACTION_HIST [0] ?
0/1 P4G_UDP_STATE_CURRENT [0] ?
0/1 P4G_UDP_STATE_TOTAL [0] ?
0/1 P4G_UDP_STATE_RATE [0] ?
0/1 P4G_UDP_RX_PAYLOAD_COUNTERS [0] ?
0/1 P4G_UDP_TX_PAYLOAD_COUNTERS [0] ?
0/1 P4G_UDP_RX_BYTES_HIST [0] ?
0/1 P4G_UDP_TX_BYTES_HIST [0] ?
0/1 P4G_TCP_RX_PACKET_COUNTERS [0] ?
0/1 P4G_TCP_TX_PACKET_COUNTERS [0] ?
0/1 P4G_UDP_RX_PACKET_COUNTERS [0] ?
0/1 P4G_UDP_TX_PACKET_COUNTERS [0] ?
0/1 P4G_CLEAR_POST_STAT [0]
0/1 P4G_RECALC_TIME_HIST [0]
0/1 P4G_RECALC_PAYLOAD_HIST [0]
0/1 P4G_RECALC_TRANSACTION_HIST [0]
0/1 P4G_REPLAY_FILE_INDICES [0] ?
0/1 P4G_REPLAY_FILE_NAME [0, 0] 'A String'
0/1 P4G_REPLAY_FILE_NAME [0, 0] ?
0/1 P4G_REPLAY_FILE_CLEAR [0]
0/1 P4G_REPLAY_UTILIZATION [0] 1
0/1 P4G_REPLAY_UTILIZATION [0] ?
0/1 P4G_REPLAY_USER_INCARNATION [0] ONCE
0/1 P4G_REPLAY_USER_INCARNATION [0] ?
0/1 P4G_REPLAY_USER_REPETITIONS [0] INFINITE 1
0/1 P4G_REPLAY_USER_REPETITIONS [0] ?
0/1 P4G_USER_STATE_CURRENT [0] ?
0/1 P4G_USER_STATE_TOTAL [0] ?
0/1 P4G_USER_STATE_RATE [0] ?
0/1 P4G_TLS_ENABLE [0] NO
0/1 P4G_TLS_ENABLE [0] ?
0/1 P4G_TLS_CIPHER_SUITES [0] 'A'
0/1 P4G_TLS_CIPHER_SUITES [0] ?
0/1 P4G_TLS_MAX_RECORD_SIZE [0] 1
0/1 P4G_TLS_MAX_RECORD_SIZE [0] ?
0/1 P4G_TLS_CERTIFICATE_FILENAME [0] 'A String'
0/1 P4G_TLS_PRIVATE_KEY_FILENAME [0] 'A String'
0/1 P4G_TLS_DHPARAMS_FILENAME [0] 'A String'
0/1 P4G_TLS_CLOSE_NOTIFY [0] NO
0/1 P4G_TLS_CLOSE_NOTIFY [0] ?
0/1 P4G_TLS_ALERT_WARNING_COUNTERS [0] ?
0/1 P4G_TLS_ALERT_FATAL_COUNTERS [0] ?
0/1 P4G_TLS_STATE_CURRENT [0] ?
0/1 P4G_TLS_STATE_TOTAL [0] ?
0/1 P4G_TLS_STATE_RATE [0] ?
0/1 P4G_TLS_RX_PAYLOAD_COUNTERS [0] ?
0/1 P4G_TLS_TX_PAYLOAD_COUNTERS [0] ?
0/1 P4G_TLS_RX_PAYLOAD_BYTES_HIST [0] ?
0/1 P4G_TLS_TX_PAYLOAD_BYTES_HIST [0] ?
0/1 P4G_TLS_HANDSHAKE_HIST [0] ?
0/1 P4G_TLS_SERVER_NAME [0] 'A String'
0/1 P4G_TLS_SERVER_NAME [0] ?
0/1 P4G_TLS_PROTOCOL_VER [0] SSLV3
0/1 P4G_TLS_PROTOCOL_VER [0] ?
0/1 P4G_TLS_MIN_REQ_PROTOCOL_VER [0] ?"""
    c_m_commands = """
0 M_EMULBYPASS OFF
0 M_EMULBYPASS ?
0 M_LATENCYMODE NORMAL
0 M_LATENCYMODE ?    
"""
    c_p_commands = """
0/1 P_EMULATE OFF
0/1 P_EMULATE ?
0/1 P_LOADMODE OFF
0/1 P_LOADMODE ?
0/1 PE_FCSDROP OFF
0/1 PE_FCSDROP ?
0/1 PE_TPLDMODE NORMAL
0/1 PE_TPLDMODE ?
0/1 PE_COMMENT [0] 'A String'
0/1 PE_COMMENT [0] ?
0/1 PE_INDICES ?
0/1 PE_LATENCYRANGE [0] ?
0/1 PE_CORRUPT [0] OFF
0/1 PE_CORRUPT [0] ?
0/1 PE_MISORDER [0] 1
0/1 PE_MISORDER [0] ?
0/1 PE_BANDPOLICER [0] OFF L1 1 1
0/1 PE_BANDPOLICER [0] ?
0/1 PE_BANDSHAPER [0] OFF L1 1 1 1
0/1 PE_BANDSHAPER [0] ?  
"""
    c_pec_commands = """
0/1 PEC_INDICES 0 1
0/1 PEC_INDICES ?
0/1 PEC_VAL [0] OFF OFF 2 0 1
0/1 PEC_VAL [0] ?
0/1 PEC_COMMENT [0] 'A String'
0/1 PEC_COMMENT [0] ?
0/1 PEC_DELETE [0]
0/1 PEC_DISTTYPE [0] ?
"""
    c_ped_commands = """
0/1 PED_SCHEDULE [0, 0] 1 1
0/1 PED_SCHEDULE [0, 0] ?
0/1 PED_ONESHOTSTATUS [0, 0] ?
0/1 PED_OFF [0, 0]
0/1 PED_FIXED [0, 0] 1
0/1 PED_FIXED [0, 0] ?
0/1 PED_RANDOM [0, 0] 1
0/1 PED_RANDOM [0, 0] ?
0/1 PED_BER [0, 0] 1 1
0/1 PED_BER [0, 0] ?
0/1 PED_FIXEDBURST [0, 0] 1
0/1 PED_FIXEDBURST [0, 0] ?
0/1 PED_RANDOMBURST [0, 0] 1 1 1
0/1 PED_RANDOMBURST [0, 0] ?
0/1 PED_GE [0, 0] 1 1 1 1
0/1 PED_GE [0, 0] ?
0/1 PED_UNI [0, 0] 1 1
0/1 PED_UNI [0, 0] ?
0/1 PED_GAUSS [0, 0] 1 1
0/1 PED_GAUSS [0, 0] ?
0/1 PED_POISSON [0, 0] 1
0/1 PED_POISSON [0, 0] ?
0/1 PED_GAMMA [0, 0] 1 1
0/1 PED_GAMMA [0, 0] ?
0/1 PED_CUST [0, 0] 1
0/1 PED_CUST [0, 0] ?
0/1 PED_CONST [0, 0] 1
0/1 PED_CONST [0, 0] ?
0/1 PED_ACCBURST [0, 0] 1
0/1 PED_ACCBURST [0, 0] ?
0/1 PED_STEP [0, 0] 1 1
0/1 PED_STEP [0, 0] ?
0/1 PED_ENABLE [0, 0] ?
"""
    c_pef_commands = """
0/1 PEF_INIT [1]
0/1 PEF_APPLY [1]
0/1 PEF_ENABLE [1,0] OFF
0/1 PEF_ENABLE [1,0] ?
0/1 PEF_ETHSETTINGS [1,0] OFF EXCLUDE
0/1 PEF_ETHSETTINGS [1,0] ?
0/1 PEF_ETHSRCADDR [1,0] OFF 0x000000000000 0xFFFFFFFFFFFF
0/1 PEF_ETHSRCADDR [1,0] ?
0/1 PEF_ETHDESTADDR [1,0] OFF 0x000000000000 0xFFFFFFFFFFFF
0/1 PEF_ETHDESTADDR [1,0] ?
0/1 PEF_L2PUSE [1,0] NA
0/1 PEF_L2PUSE [1,0] ?
0/1 PEF_VLANSETTINGS [1,0] OFF EXCLUDE
0/1 PEF_VLANSETTINGS [1,0] ?
0/1 PEF_VLANTAG [1,0,0] OFF 0 0x0FFF
0/1 PEF_VLANTAG [1,0,0] ?
0/1 PEF_VLANPCP [1,0,0] OFF 0 0x07
0/1 PEF_VLANPCP [1,0,0] ?
0/1 PEF_MPLSSETTINGS [1,0] OFF EXCLUDE
0/1 PEF_MPLSSETTINGS [1,0] ?
0/1 PEF_MPLSLABEL [1,0] OFF 0 0x0FFFFF
0/1 PEF_MPLSLABEL [1,0] ?
0/1 PEF_MPLSTOC [1,0] OFF 0 0x07
0/1 PEF_MPLSTOC [1,0] ?
0/1 PEF_L3USE [1,0] IP4
0/1 PEF_L3USE [1,0] ?
0/1 PEF_IPV4SETTINGS [1,0] OFF EXCLUDE
0/1 PEF_IPV4SETTINGS [1,0] ?
0/1 PEF_IPV4SRCADDR [1,0] OFF 192.168.1.100 0xFFFFFFFF
0/1 PEF_IPV4SRCADDR [1,0] ?
0/1 PEF_IPV4DESTADDR [1,0] OFF 192.168.1.100 0xFFFFFFFF
0/1 PEF_IPV4DESTADDR [1,0] ?
0/1 PEF_IPV4DSCP [1,0] OFF 0 0xFC
0/1 PEF_IPV4DSCP [1,0] ?
0/1 PEF_IPV6SETTINGS [1,0] OFF EXCLUDE
0/1 PEF_IPV6SETTINGS [1,0] ?
0/1 PEF_IPV6SRCADDR [1,0] OFF 0x00000000000000000000000000000000 0xFFFFFFFFFFFFFFFFFFFFFFFFF
0/1 PEF_IPV6SRCADDR [1,0] ?
0/1 PEF_IPV6DESTADDR [1,0] OFF 0x00000000000000000000000000000000 0xFFFFFFFFFFFFFFFFFFFFFFFF
0/1 PEF_IPV6DESTADDR [1,0] ?
0/1 PEF_IPV6TC [1,0] OFF 0 0xFC
0/1 PEF_IPV6TC [1,0] ?
0/1 PEF_UDPSETTINGS [1,0] OFF EXCLUDE
0/1 PEF_UDPSETTINGS [1,0] ?
0/1 PEF_UDPSRCPORT [1,0] OFF 0 0xFFFF
0/1 PEF_UDPSRCPORT [1,0] ?
0/1 PEF_UDPDESTPORT [1,0] OFF 0 0xFFFF
0/1 PEF_UDPDESTPORT [1,0] ?
0/1 PEF_TCPSETTINGS [1,0] OFF EXCLUDE
0/1 PEF_TCPSETTINGS [1,0] ?
0/1 PEF_TCPSRCPORT [1,0] OFF 0 0xFFFF
0/1 PEF_TCPSRCPORT [1,0] ?
0/1 PEF_TCPDESTPORT [1,0] OFF 0 0xFFFF
0/1 PEF_TCPDESTPORT [1,0] ?
0/1 PEF_ANYSETTINGS [1,0] OFF EXCLUDE
0/1 PEF_ANYSETTINGS [1,0] ?
0/1 PEF_ANYCONFIG [1,0] 0 0x000000000000 0xFFFFFFFFFFFF
0/1 PEF_ANYCONFIG [1,0] ?
0/1 PEF_TPLDSETTINGS [1,0] OFF EXCLUDE
0/1 PEF_TPLDSETTINGS [1,0] ?
0/1 PEF_TPLDCONFIG [1,0,0] OFF 0
0/1 PEF_TPLDCONFIG [1,0,0] ?
0/1 PEF_VALUE [1,0,1] 0x000000000000000000000000 
0/1 PEF_VALUE [1,0,1] ?
0/1 PEF_MASK [1,0,1] 0xFFFFFFFFFFFFFFFFFFFFFFFF
0/1 PEF_MASK [1,0,1] ?
0/1 PEF_PROTOCOL [1,0] ETHERNET VLAN ECPRI
0/1 PEF_PROTOCOL [1,0] ?
0/1 PEF_MODE [1,0] BASIC
0/1 PEF_MODE [1,0] ?
0/1 PEF_ISSHADOWDIRTY [1] ?
0/1 PEF_CANCEL [1]
"""
    c_pe_commands = """
0/1 PE_CLEAR
0/1 PE_DUPTOTAL ?
0/1 PE_MISTOTAL ?
0/1 PE_CORTOTAL ?
0/1 PE_JITTERTOTAL ?
0/1 PE_LATENCYTOTAL ?
0/1 PE_DROPTOTAL ?    
"""
    c_pee_commands = """
0/1 PE_FLOWDROPTOTAL [0] ?
0/1 PE_FLOWLATENCYTOTAL [0] ?
0/1 PE_FLOWDUPTOTAL [0] ?
0/1 PE_FLOWMISTOTAL [0] ?
0/1 PE_FLOWCORTOTAL [0] ?
0/1 PE_FLOWJITTERTOTAL [0] ?
0/1 PE_FLOWCLEAR [0]    
"""
    c_pt_commands = """
0/1 PT_FLOWTOTAL [0] ?
0/1 PT_FLOWCLEAR [0]    
"""
    c_pr_commands = """
0/1 PR_FLOWTOTAL [0] ?
0/1 PR_FLOWCLEAR [0]
"""
    all_commands = (
        c_commands
        + m_commands
        + p_commands
        + pc_commands
        + pd_commands
        + pf_commands
        + pl_commands
        + pm_commands
        + pp_commands
        + ps_commands
        + pt_commands
        + pr_commands
        + px_commands
        + pl1_commands
        + m4_commands
        + m4e_commands
        + p4_commands
        + p4e_commands
        + p4g_commands
        + c_m_commands
        + c_p_commands
        + c_pec_commands
        + c_ped_commands
        + c_pef_commands
        + c_pe_commands
        + c_pee_commands
        + c_pt_commands
        + c_pr_commands
    )
    # for c in CLIConverter.read_commands_from_string(all_commands):
    #     print(c)
    #     print(c.as_request())

    with open("./all_commands.txt", "w") as f:
        f.write(all_commands)
    for c in CLIConverter.read_commands_from_file("./all_commands.txt"):
        print(c)
        print(c.as_request())
    os.unlink("./all_commands.txt")


def run(method: Coroutine) -> None:
    import platform

    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(method)

if __name__ == "__main__":
    run(test_config_cli())