import re
import html

class SecurityUtils:
    
    @staticmethod
    def sanitize_for_prompt(text: str) -> str:
        """
        Prevents Stored Prompt Injection by escaping HTML/XML tags.
        If a bad memory tries to close the <past_learnings> tag, this neutralizes it.
        """
        # Converts <script> to &lt;script&gt; so the LLM reads it as text, not code.
        return html.escape(text)

    @staticmethod
    def scrub_sensitive_data(text: str) -> str:
        """
        Removes PII and Secrets from the diff before sending to Pinecone.
        """
        # 1. Redact Email Addresses
        text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[REDACTED_EMAIL]', text)
        
        # 2. Redact IP Addresses (IPv4)
        text = re.sub(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', '[REDACTED_IP]', text)
        
        # 3. Redact Common API Keys (Generic "sk-" or "ghp_" patterns)
        text = re.sub(r'(sk-[a-zA-Z0-9]{20,})', '[REDACTED_KEY]', text)
        text = re.sub(r'(ghp_[a-zA-Z0-9]{20,})', '[REDACTED_KEY]', text)
        
        return text