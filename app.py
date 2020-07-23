<<<<<<< HEAD
"""Main application file"""
from flask import Flask
app = Flask(__name__)

@app.route('/<random_string>')
def returnBackwardsString(random_string):
    """Reverse and return the provided URI"""
    return "".join(reversed(random_string))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
=======
#!/usr/bin/env python3

from aws_cdk import core

from ecs_devops_sandbox_cdk.ecs_devops_sandbox_cdk_stack import EcsDevopsSandboxCdkStack


app = core.App()
EcsDevopsSandboxCdkStack(app, "ecs-devops-sandbox-cdk")

app.synth()
>>>>>>> gerar-error
