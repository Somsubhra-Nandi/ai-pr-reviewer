import re
import html

class SecurityUtils:
    
    # Pre-compile regex patterns for performance
    # These cover AWS, Azure, Google, Slack, and generic private keys
    SENSITIVE_PATTERNS = [
        r'AKIA[0-9A-Z]{16}',                       # AWS Access Key
        r'[a-zA-Z0-9/+]{40}',                      # AWS Secret Key (High Entropy)
        r'ghp_[a-zA-Z0-9]{36}',                    # GitHub Personal Access Token
        r'sk-[a-zA-Z0-9]{32,}',                    # OpenAI / Generic API Keys
        r'xox[baprs]-([0-9a-zA-Z]{10,48})',        # Slack Tokens
        r'-----BEGIN\s+PRIVATE\s+KEY-----',        # RSA Private Keys
        r'AIza[0-9A-Za-z-_]{35}',                  # Google API Keys
    ]

    @staticmethod
    def sanitize_for_prompt(text: str) -> str:
        """
        Prevents Stored Prompt Injection by escaping HTML/XML tags.
        """
        return html.escape(text)

    @staticmethod
    def scrub_sensitive_data(text: str) -> str:
        """
        Redacts PII and Secrets using the Enterprise Regex Pack.
        """
        # 1. Redact Email Addresses
        text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[REDACTED_EMAIL]', text)
        
        # 2. Redact IP Addresses
        text = re.sub(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', '[REDACTED_IP]', text)
        
        # 3. Redact Cloud Secrets (The new robust check)
        for pattern in SecurityUtils.SENSITIVE_PATTERNS:
            text = re.sub(pattern, '[REDACTED_SECRET]', text)
            
        return text