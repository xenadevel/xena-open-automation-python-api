import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import enums
from xoa_driver import utils
from xoa_driver.hlfuncs import mgmt, cli

async def my_awesome_func(stop_event: asyncio.Event):
    # create tester instance and establish connection
    async with testers.L23Tester("10.10.10.10", "xoa") as tester:

        # access module 0 on the tester
        module = tester.modules.obtain(0)
        if isinstance(module, modules.ModuleChimera):
            return None
        
        # access port 0 on the module
        port = module.ports.obtain(0) 

        # reserve the port
        await mgmt.reserve_port(port=port)

        # configure port with .xpc file generated by ValkyrieManager
        await cli.port_config_from_file(port=port, path="port_config.xpc")

        # configure port with CLI commands
        await cli.port_config_from_string(
            port=port,
            long_str="""
            P_RESET
            P_COMMENT \"this is a comment\"
            P_MACADDRESS  0xAAAAAABBBB99
            P_IPADDRESS  1.1.1.1 0.0.0.0 0.0.0.0 0.0.0.0
            """)
        
        # reserve the module
        await mgmt.reserve_module(module=module)

        # configure module by file
        await cli.module_config_from_file(module=module, path="module_config.txt")

        # configure module with CLI commands
        await cli.module_config_from_string(
            module=module,
            long_str="""
            M_COMMENT \"this is a comment\"
            M_MEDIA  QSFP_DD_NRZ
            M_CFPCONFIGEXT  2 100000 100000
            """)
        
        # reserve the tester
        await mgmt.reserve_tester(tester=tester)

        # configure module by file
        await cli.tester_config_from_file(tester=tester, path="tester_config.txt")

        # configure module with CLI commands
        await cli.tester_config_from_string(
            tester=tester,
            long_str="""
            C_COMMENT \"this is a comment\"
            C_NAME \"this is a name\"
            """)

async def main():
    stop_event = asyncio.Event()
    try:
        await my_awesome_func(stop_event)
    except KeyboardInterrupt:
        stop_event.set()


if __name__ == "__main__":
    asyncio.run(main())