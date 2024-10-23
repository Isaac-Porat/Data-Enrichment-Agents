import json
from anthropic.types.tool_use_block import ToolUseBlock

from tools.create_column import create_column
from tools.write_column import write_column
from tools.read_column import read_column
from tools.research import scrape_website
from tools.ask_user import ask_user


def load_schema(schema_path: str) -> dict:
    with open(schema_path, "r") as file:
        schema = json.load(file)
    return schema

ask_user_schema = load_schema("/Users/zakporat/Documents/current_projects/data_enrichment_agents/app/tools/schema/ask_user.json")
create_column_schema = load_schema("/Users/zakporat/Documents/current_projects/data_enrichment_agents/app/tools/schema/create_column.json")
write_column_schema = load_schema("/Users/zakporat/Documents/current_projects/data_enrichment_agents/app/tools/schema/write_column.json")
read_column_schema = load_schema("/Users/zakporat/Documents/current_projects/data_enrichment_agents/app/tools/schema/read_column.json")
research_schema = load_schema("/Users/zakporat/Documents/current_projects/data_enrichment_agents/app/tools/schema/research.json")

def use_tool(tool_use_content: ToolUseBlock) -> dict:
    print(f"Tool use Block: {tool_use_content}")

    tools_map = {
        "ask_user": ask_user,
        "create_column": create_column,
        "write_column": write_column,
        "read_column": read_column,
        "scrape_website": scrape_website
    }

    tool_name = tool_use_content.name
    tool_input = tool_use_content.input
    tool_function = tools_map[tool_name]

    return tool_function(**tool_input)