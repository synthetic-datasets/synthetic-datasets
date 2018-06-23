

# Synthetic Datasets


* NoiseCircle


## NoiseCircle

A generator of square images, by default 64x64, with static noise and a circle
with noisy pixels in the image at a random location and with a random size.

Each result from the generator is a square numpy matrix of type float32

Example use::

```
    from synthetic_datasets import NoiseCircle

    nc = NoiseCircle()
    for image in nc:
        // Use image
```

## Licence
MIT


## More info
- https://github.com/synthetic-datasets/synthetic-datasets
- https://www.meetup.com/Toronto-AI/
- http://torontoai.org/
- A Toronto AI initiative
