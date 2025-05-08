#request,调用本地localhost:5000/submit
import json
import os
import requests
import logging
from mcp.server.fastmcp import FastMCP

# 配置日志
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.debug("Starting Submit qasm task click initialization")


# 初始化MCP服务器
try:
    logger.debug("Submit qasm task")
    mcp = FastMCP("qasm_submit")
    logger.debug("FastMCP initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize FastMCP: {e}")
    raise

# 定义乘法工具
@mcp.tool()
def qasm_submit(qasm_str, user_name, private_key) -> json:
    """submit qasm task to spinq cloud"""
    logger.debug(f"submit qasm task to spinq cloud with qasm_str={qasm_str}")

    res = requests.post(
        "https://uat-cloud.spinq.cn:5000/submit",
        json={
            "qasm_str": qasm_str,
            "optimization_level": 0,
            "user_name": user_name,
            "private_key": private_key
        })
    if res.status_code == 200:
        return res.json()
    else:
        logger.error(f"Error: {res.status_code}, {res.text}")
        return {
            "error": "Failed to submit qasm task",
            "status_code": res.status_code,
            "text": res.text
        }
        

logger.debug("Tool registered")

if __name__ == "__main__":
  try:
    logger.debug("Starting MCP server with stdio transport")
    # mcp.run(transport='stdio')
    mcp.run(transport='sse')
    logger.debug("MCP server exited normally")
  except Exception as e:
    logger.error(f"MCP server failed: {e}")
    raise