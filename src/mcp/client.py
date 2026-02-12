import logging

logger = logging.getLogger("mcp_client")

class MCPClient:
    def __init__(self, repo_name: str):
        self.repo_name = repo_name

    async def get_pr_diff(self, pr_number: int) -> str:
        # A "Safe" Diff (Refactoring code, no secrets)
        return """
        diff --git a/src/main.py b/src/main.py
        index 83c5a9..b2d1f4 100644
        --- a/src/main.py
        +++ b/src/main.py
        @@ -10,4 +10,4 @@
        -def hello():
        -    print("Hello world")
        +def hello(name):
        +    print(f"Hello {name}")
        """

    async def post_comment(self, pr_number: int, review) -> str:
        """
        MOCK GITHUB:
        Instead of posting to GitHub, it prints the formatted review to your console.
        """
        logger.info(f"🚀 MCP: Posting comment to PR #{pr_number}...")
        
        # This print block mimics what would appear on GitHub
        print("\n" + "="*60)
        print(f"🤖 AI REVIEW FOR PR #{pr_number}")
        print(f"📊 Security Score: {getattr(review, 'security_score', 'N/A')}/100")
        print(f"📝 Summary: {getattr(review, 'summary', 'No summary')}")
        print("-" * 60)
        
        # Safely loop through findings if they exist
        findings = getattr(review, 'findings', [])
        for finding in findings:
            print(f"[{finding.severity}] {finding.file_path}:{finding.line_start}")
            print(f"   💡 {finding.suggestion}")
        print("="*60 + "\n")
        
        return "https://github.com/mock/comment/1"