import subprocess

# loading first 10,000 sentences of corpus

def load_corpus_en_es(n=10_000):
    cmd = [
        "opus_read",
        "--directory", "Tatoeba",
        "--source", "en",
        "--target", "es",
        "--write_mode", "moses",
        "-m", str(n),
        "-q",
    ]

    try:
        proc = subprocess.run(cmd, text=True, capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit status {e.returncode}")
        print(f"stderr: {e.stderr}")
        raise

    en, es = [], []
    for line in proc.stdout.splitlines():
        if "\t" in line:
            a, b = line.split("\t", 1)
            en.append(a.strip())
            es.append(b.strip())
        if len(en) >= n:
            break

    return en, es


# Save corpus to text files
if __name__ == "__main__":
    en, es = load_corpus_en_es()
    
    with open("corpus_en.txt", "w") as f:
        f.write("\n".join(en))
    
    with open("corpus_es.txt", "w") as f:
        f.write("\n".join(es))
    
    print(f"Saved {len(en)} English sentences to corpus_en.txt")
    print(f"Saved {len(es)} Spanish sentences to corpus_es.txt")

