import re

def extract_features(url):
    features = []

    features.append(len(url))
    features.append(url.count('.'))
    features.append(url.count('-'))
    features.append(1 if "@" in url else 0)
    features.append(1 if url.startswith("https") else 0)

    keywords = ["login", "verify", "bank", "secure", "account"]
    features.append(sum(word in url.lower() for word in keywords))

    features.append(sum(c.isdigit() for c in url))

    ip_pattern = r'\d+\.\d+\.\d+\.\d+'
    features.append(1 if re.search(ip_pattern, url) else 0)

    return features