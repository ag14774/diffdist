# diffdist

## NOTE: PyTorch now includes the distributed RPC framework (https://pytorch.org/docs/stable/rpc.html). Most tasks can now be achieved using RPC. If you need a simpler MPI-like alternative, `diffdist` is for you!

`diffdist` is a python library for pytorch. It extends the default functionality of `torch.autograd` and adds support for differentiable communication between processes. This enables backpropagation to work in distributed settings and makes it super easy to use distributed model parallelism! `diffdist` achieves that by simply implementing the backward passes for most common communication primitives of `torch.distributed`. Processes that communicate during the forward pass, will automatically communicate during the backward pass to exchange gradients.

### Installation

After installing `pytorch` install simply using:

```sh
$ pip install diffdist
```

### Examples
You can find examples on how to use `diffdist` in `diffdist/testing.py`

License
----

GNU GPLv3

