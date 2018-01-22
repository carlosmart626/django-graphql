from promise import Promise


def depromise_subscription(next, root, info, **args):
    result = next(root, info, **args)
    if info.operation.operation == 'subscription' and isinstance(result, Promise):
        return result.get()
    return result
