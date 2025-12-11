#!/bin/bash

# Pico: Smallest model, can use large batch sizes directly
# Recommended: batch=1024, grad_accum=1, warmup=2
uv run modal \
	run --detach modal_train.py \
	--model-size pico \
	--calculate-batch \
	--epochs 20 \
	--gradient-accumulation-steps 4 \
	--warmup-epochs 2

# Nano: Small model, moderate batch with slight accumulation
# Recommended: batch=512, grad_accum=2 (effective=1024), warmup=3
uv run modal \
	run --detach modal_train.py \
	--model-size nano \
	--calculate-batch \
	--epochs 20 \
	--gradient-accumulation-steps 4 \
	--warmup-epochs 3
