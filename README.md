# diffdist

# NOTE: PyTorch now includes the distributed RPC framework (https://pytorch.org/docs/stable/rpc.html). You are highly encouraged to switch to that. Thank you for using `diffdist`!

`diffdist` is a python library for pytorch. It extends the default functionality of `torch.autograd` and adds support for differentiable communication between processes. This enables backpropagation to work in distributed settings and makes it super easy to use distributed model parallelism!

### Installation

After installing `pytorch` install simply using:

```sh
$ pip install diffdist
```

License
----

GNU GPLv3

