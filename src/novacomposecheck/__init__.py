from pathlib import Path
import yaml
import typer
app=typer.Typer(no_args_is_help=True)
@app.command()
def check(file: Path)->None:
    data=yaml.safe_load(file.read_text()) or {}; findings=[]
    for name,service in (data.get("services") or {}).items():
        if service.get("privileged"): findings.append(f"{name}: privileged mode")
        if service.get("network_mode")=="host": findings.append(f"{name}: host networking")
        for volume in service.get("volumes",[]):
            if "/var/run/docker.sock" in str(volume): findings.append(f"{name}: Docker socket mounted")
        for port in service.get("ports",[]):
            if str(port).split(":")[-1].split("/")[0] in {"5432","3306","27017","6379"}: findings.append(f"{name}: database/cache port published ({port})")
    for finding in findings: typer.echo("WARNING "+finding)
    if not findings: typer.echo("No configured checks triggered.")
