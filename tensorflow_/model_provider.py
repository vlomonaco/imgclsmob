from .models.resnet import *
from .models.preresnet import *
from .models.densenet import *
from .models.darknet import *
from .models.squeezenet import *
from .models.mobilenet import *
from tensorflow_.models.others.shufflenetv2 import *

__all__ = ['get_model']


_models = {
    'resnet10': resnet10,
    'resnet12': resnet12,
    'resnet14': resnet14,
    'resnet16': resnet16,
    'resnet18_wd4': resnet18_wd4,
    'resnet18_wd2': resnet18_wd2,
    'resnet18_w3d4': resnet18_w3d4,

    'resnet18': resnet18,
    'resnet34': resnet34,
    'resnet50': resnet50,
    'resnet50b': resnet50b,
    'resnet101': resnet101,
    'resnet101b': resnet101b,
    'resnet152': resnet152,
    'resnet152b': resnet152b,
    'resnet200': resnet200,
    'resnet200b': resnet200b,

    'seresnet18': seresnet18,
    'seresnet34': seresnet34,
    'seresnet50': seresnet50,
    'seresnet50b': seresnet50b,
    'seresnet101': seresnet101,
    'seresnet101b': seresnet101b,
    'seresnet152': seresnet152,
    'seresnet152b': seresnet152b,
    'seresnet200': seresnet200,
    'seresnet200b': seresnet200b,

    'preresnet10': preresnet10,
    'preresnet12': preresnet12,
    'preresnet14': preresnet14,
    'preresnet16': preresnet16,
    'preresnet18_wd4': preresnet18_wd4,
    'preresnet18_wd2': preresnet18_wd2,
    'preresnet18_w3d4': preresnet18_w3d4,

    'preresnet18': preresnet18,
    'preresnet34': preresnet34,
    'preresnet50': preresnet50,
    'preresnet50b': preresnet50b,
    'preresnet101': preresnet101,
    'preresnet101b': preresnet101b,
    'preresnet152': preresnet152,
    'preresnet152b': preresnet152b,
    'preresnet200': preresnet200,
    'preresnet200b': preresnet200b,

    'sepreresnet18': sepreresnet18,
    'sepreresnet34': sepreresnet34,
    'sepreresnet50': sepreresnet50,
    'sepreresnet50b': sepreresnet50b,
    'sepreresnet101': sepreresnet101,
    'sepreresnet101b': sepreresnet101b,
    'sepreresnet152': sepreresnet152,
    'sepreresnet152b': sepreresnet152b,
    'sepreresnet200': sepreresnet200,
    'sepreresnet200b': sepreresnet200b,

    'densenet121': densenet121,
    'densenet161': densenet161,
    'densenet169': densenet169,
    'densenet201': densenet201,

    'darknet_ref': darknet_ref,
    'darknet_tiny': darknet_tiny,
    'darknet19': darknet19,

    'squeezenet_v1_0': squeezenet_v1_0,
    'squeezenet_v1_1': squeezenet_v1_1,

    'squeezeresnet_v1_0': squeezeresnet_v1_0,
    'squeezeresnet_v1_1': squeezeresnet_v1_1,

    'mobilenet_w1': mobilenet_w1,
    'mobilenet_w3d4': mobilenet_w3d4,
    'mobilenet_wd2': mobilenet_wd2,
    'mobilenet_wd4': mobilenet_wd4,

    'fdmobilenet_w1': fdmobilenet_w1,
    'fdmobilenet_w3d4': fdmobilenet_w3d4,
    'fdmobilenet_wd2': fdmobilenet_wd2,
    'fdmobilenet_wd4': fdmobilenet_wd4,

    'shufflenetv2_wd2': shufflenetv2_wd2,
}


def get_model(name, **kwargs):
    """
    Get supported model.

    Parameters:
    ----------
    name : str
        Name of model.

    Returns
    -------
    HybridBlock
        Resulted model.
    """
    name = name.lower()
    if name not in _models:
        raise ValueError('Unsupported model: {}'.format(name))
    net = _models[name](**kwargs)
    return net
