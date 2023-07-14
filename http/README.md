# To install:

## Install torch and requirements on CUDA environments

```
pip install --index-url https://download.pytorch.org/whl/nightly/cu118 --pre 'torch>=2.1.0dev'
pip install -r requirements.txt
```

## Download the models
`python scripts/download.py --repo_id  tiiuae/falcon-7b-instruct`

## Do some data conversiong
`python scripts/convert_hf_checkpoint.py --checkpoint_dir checkpoints/tiiuae/falcon-7b-instruct`

## Run generation
`python generate/base.py --checkpoint_dir checkpoints/tiiuae/falcon-7b-instruct --prompt "Hello, my name is"`

# Run the HTTP endpoint application:

`uvicorn app:app --host 0.0.0.0`

