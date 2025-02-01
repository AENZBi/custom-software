import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Automates the setup of the Aenzbi-Business project'

    def handle(self, *args, **kwargs):
        project_name = 'aenzbi-business'
        self.stdout.write(f'Setting up project: {project_name}')

        # Create directory structure
        self.create_directory_structure()

        # Create common files
        self.create_common_files()

        # Backend setup
        self.setup_backend()

        # Web app setup
        self.setup_web()

        # Mobile app setup
        self.setup_mobile()

        self.stdout.write(self.style.SUCCESS('Project setup completed successfully!'))

    def create_directory_structure(self):
        project_structure = [
            f"{project_name}/backend/api/banking",
            f"{project_name}/backend/api/microfinance",
            f"{project_name}/backend/api/money-transfer",
            f"{project_name}/backend/api/fintech-crypto",
            f"{project_name}/backend/api/payments",
            f"{project_name}/backend/api/sales",
            f"{project_name}/backend/api/e-billing",
            f"{project_name}/backend/api/e-shop",
            f"{project_name}/backend/config",
            f"{project_name}/backend/db",
            f"{project_name}/backend/middlewares",
            f"{project_name}/backend/models",
            f"{project_name}/backend/tests",
            f"{project_name}/web/public",
            f"{project_name}/web/src/components",
            f"{project_name}/web/src/pages",
            f"{project_name}/web/src/services",
            f"{project_name}/web/src/styles",
            f"{project_name}/web/src/utils",
            f"{project_name}/mobile/android",
            f"{project_name}/mobile/ios",
            f"{project_name}/mobile/lib/components",
            f"{project_name}/mobile/lib/pages",
            f"{project_name}/mobile/lib/services",
            f"{project_name}/mobile/lib/styles",
            f"{project_name}/docs",
            f"{project_name}/scripts/db-migrations",
            f"{project_name}/scripts/deployment",
            f"{project_name}/firebase"
        ]

        for directory in project_structure:
            os.makedirs(directory, exist_ok=True)
            self.stdout.write(f'Created directory: {directory}')

    def create_common_files(self):
        with open("README.md", "w") as f:
            f.write("# aenzbi-business\n\n")
            f.write("A comprehensive system for banking, microfinance, money transfer, fintech, crypto, and e-commerce.\n\n")
            f.write("## Features\n")
            f.write("- Banking and Microfinance\n")
            f.write("- Money Transfer and Fintech Integration\n")
            f.write("- E-Shop, E-Billing, Sales, and Payments\n")
            f.write("- Wallet and Visa Card Support\n\n")
            f.write("## Setup Instructions\n")
            f.write("Run the provided management command to set up the entire project.\n")
        
        open(".gitignore", "w").close()
        open(".env.example", "w").close()
        open("LICENSE", "w").close()

    def setup_backend(self):
        # This function would initialize backend requirements and create files/settings.
        backend_directory = "backend"
        os.chdir(backend_directory)
        # This is where you would typically manage dependencies or installations (if needed).

        # Create app.py for backend (for demonstration)
        with open("app.py", "w") as f:
            f.write("from django.core.management import execute_from_command_line\n")
            f.write("import os\n")
            f.write("import sys\n\n")
            f.write("if __name__ == '__main__':\n")
            f.write("    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')\n")
            f.write("    execute_from_command_line(sys.argv)\n")

        # Create routes for banking
        os.makedirs("api/banking", exist_ok=True)
        with open("api/banking/routes.py", "w") as f:
            f.write("from django.http import JsonResponse\n\n")
            f.write("def accounts(request):\n")
            f.write("    return JsonResponse({'message': 'List of banking accounts'})\n")

    def setup_web(self):
        os.chdir("../web")
        os.system("npx create-react-app .")
        os.system("npm install react-router-dom axios")

        web_src_path = "src/pages/"
        os.makedirs(web_src_path, exist_ok=True)
        with open(f"{web_src_path}/Banking.js", "w") as f:
            f.write("import React from 'react';\n\n")
            f.write("function Banking() {\n")
            f.write("  return (\n")
            f.write("    <div>\n")
            f.write("      <h1>Banking Module</h1>\n")
            f.write("      <p>Manage accounts, transactions, and loans here.</p>\n")
            f.write("    </div>\n")
            f.write("  );\n")
            f.write("}\n\n")
            f.write("export default Banking;\n")

    def setup_mobile(self):
        os.chdir("../mobile")
        os.system("flutter create .")

        os.chdir("lib")
        with open("main.dart", "w") as f:
            f.write("import 'package:flutter/material.dart';\n\n")
            f.write("void main() {\n")
            f.write("  runApp(const MyApp());\n")
            f.write("}\n\n")
            f.write("class MyApp extends StatelessWidget {\n")
            f.write("  const MyApp({super.key});\n\n")
            f.write("  @override\n")
            f.write("  Widget build(BuildContext context) {\n")
            f.write("    return MaterialApp(\n")
            f.write("      title: 'Aenzbi-Business',\n")
            f.write("      home: Scaffold(\n")
            f.write("        appBar: AppBar(\n")
            f.write("          title: const Text('Aenzbi-Business'),\n")
            f.write("        ),\n")
            f.write("        body: const Center(\n")
            f.write("          child: Text('Welcome to Aenzbi-Business'),\n")
            f.write("        ),\n")
            f.write("      ),\n")
            f.write("    );\n")
            f.write("  }\n")
            f.write("}\n")p