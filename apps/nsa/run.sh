uv run modal \
	run modal_train.py \
	--model-size pico \
	--batch-size 1024 \
	--epochs 20

uv run modal \
	run modal_train.py \
	--model-size nano \
	--batch-size 512 \
	--epochs 20

uv run modal \
	run modal_train.py \
	--model-size tiny \
	--batch-size 256 \
	--epochs 20
