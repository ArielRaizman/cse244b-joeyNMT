import os
import random

def prepare_joey_data(input_file, src_lang="en", trg_lang="es", split_ratio=(0.8, 0.1, 0.1)):
    src_lines = []
    trg_lines = []

    # 1. Parse the TSV
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 4:
                # Based on your snippet: ID, SRC, ID, TRG
                src_lines.append(parts[1].strip())
                trg_lines.append(parts[3].strip())

    # 2. Shuffle and Split
    combined = list(zip(src_lines, trg_lines))
    random.seed(42) # For reproducibility
    random.shuffle(combined)

    total = len(combined)
    train_end = int(total * split_ratio[0])
    dev_end = train_end + int(total * split_ratio[1])

    sets = {
        'train': combined[:train_end],
        'dev': combined[train_end:dev_end],
        'test': combined[dev_end:]
    }

    # 3. Save Files
    for set_name, data in sets.items():
        if not data: continue
        
        for i, lang in enumerate([src_lang, trg_lang]):
            filename = f"{set_name}.{lang}"
            with open(filename, 'w', encoding='utf-8') as out_f:
                for item in data:
                    out_f.write(item[i] + '\n')
            print(f"Created {filename} with {len(data)} lines.")

if __name__ == "__main__":
    # Ensure your file is named en-es.tsv in the same directory
    prepare_joey_data('en-es.tsv')