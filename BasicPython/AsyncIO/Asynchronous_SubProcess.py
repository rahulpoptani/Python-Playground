# The asyncio.subprocess.Process class provides a representation of a subprocess run by asyncio.

# There are two ways to execute an external program as a subprocess and acquire a Process instance, they are:
    # asyncio.create_subprocess_exec() for running commands directly.
    # asyncio.create_subprocess_shell() for running commands via the shell.

import asyncio

async def main():
    process = await asyncio.create_subprocess_exec('echo', 'Hello World')
    print(f'subprocess: {process}')

asyncio.run(main())