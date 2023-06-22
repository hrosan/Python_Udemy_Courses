'''
    Modularization, in the context of software development, refers to the practice of dividing a program into 
separate modules or components. Each module focuses on a specific functionality or feature, making the overall 
program more organized, maintainable, and reusable.

The main benefits of modularization include:
    * Code organization: Modularization helps break down a complex program into smaller, manageable parts. 
Each module can be developed, tested, and maintained independently, making it easier to understand and work with the 
codebase.
    * Code reusability: By dividing the program into modules, you can create reusable components. 
These modules can be used in multiple projects or within the same project to avoid duplicating code. This saves 
time and effort, promotes code consistency, and reduces the chances of introducing bugs.
    * Collaboration: Modularization enables teams to work on different modules simultaneously, allowing for 
parallel development. Each team member can focus on a specific module, improving productivity and coordination.
    * Maintenance and troubleshooting: When an issue or bug arises, modularization allows you to pinpoint the 
specific module where the problem is occurring. This makes troubleshooting and bug fixing more efficient, as you can 
isolate and address issues in specific modules without affecting the rest of the program.

    To achieve modularization in Python, you can create separate Python files, each containing a module or component. 
These files can be imported and used in other parts of the program as needed. This approach promotes code organization,
reusability, and maintainability.

    By following modularization principles, you can create well-structured, scalable, and maintainable codebases, 
making your programs more robust and easier to work with.
'''
from teste_main import soma

print("Este modulo se chama:", __name__)

soma(5,7)

