import json
from pathlib import Path
from typer import Typer
from typer import Argument,Option
from typing import Annotated, List
from model import get_session, ConfigMeta
from sqlmodel import Session
app = Typer(
    name="easy_config",
    no_args_is_help=True
)




@app.command("add",no_args_is_help=True)
def create_config(
    name: Annotated[str,Argument(show_default=False)],
    path: Annotated[
        List[str], 
        Option(
            "--path",
            "-p",
            show_default=False,
            help="config file or folder path",
        )
    ] = [],
    session: Session =get_session()
):
    """
    添加配置文件记录
    """
    
    print(name)
    print(path)

@app.command("ls")
def list_configs(config_name: Annotated[str,Option()]):
    """
    查看所有配置
    """
    

    
if __name__ == "__main__":
    app()