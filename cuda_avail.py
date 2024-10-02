#!/usr/bin/env python3
import torch

if __name__ == "__main__":
    res = torch.cuda.is_available()
    
    print(f"Is cuda available?\n\t{res}")
