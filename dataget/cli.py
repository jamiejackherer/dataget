#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xdf06bef7

# Compiled with Coconut version 1.2.2-post_dev12 [Colonel]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_pipe, _coconut_starpipe, _coconut_backpipe, _coconut_backstarpipe, _coconut_bool_and, _coconut_bool_or, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------

import click
click.disable_unicode_literals_warning = True

import os

from dataget.api import ls as _ls
from dataget.api import data
from dataget.api import get_path

@click.group()
@click.option('--path', '-p', default=None)
@click.option('-g', is_flag=True, help="Use global path: DATAGET_HOME env variable or ~/.dataget by default.")
@click.pass_context
def main(ctx, path, g):
    path = get_path(path=path, global_=g)
    ctx.obj = dict(path=path, global_=g)


@main.command()
@click.option('--available', '-a', is_flag=True, help="List all available dataget datasets for download.")
@click.pass_context
def ls(ctx, available):
    "List installed datasets on path"

    path = ctx.obj['path']
    global_ = ctx.obj['global_']

    _ls(available=available, path=path, global_=global_)

@main.command()
@click.argument('dataset')
@click.argument('kwargs', nargs=-1)
@click.pass_context
def reqs(ctx, dataset, kwargs):
    "Get the dataset's pip requirements"

    kwargs = parse_kwargs(kwargs)
    (print)(data(dataset, ctx.obj["path"]).reqs(**kwargs))


@main.command()
@click.argument('dataset')
@click.option('--clear', '-c', is_flag=True, help="removes the dataset's folder (if it exists) before downloading")
@click.option('--keep-compressed', is_flag=True, help="keeps the compressed files: skips remove_compressed")
@click.option('--dont-process', is_flag=True, help="skips process")
@click.option('--keep-raw', is_flag=True, help="keeps the raw/unprocessed files: skips remove_raw")
@click.argument('kwargs', nargs=-1)
@click.pass_context
def get(ctx, dataset, clear, keep_compressed, dont_process, keep_raw, kwargs):
    "performs the operations download, extract, remove_compressed, processes and remove_raw, in sequence. KWARGS must be in the form: key=value, and are fowarded to all opeartions."

    kwargs = parse_kwargs(kwargs)

    process = not dont_process
    remove_raw = not keep_raw
    remove_compressed = not keep_compressed

    data(dataset, ctx.obj["path"]).get(clear=clear, remove_compressed=remove_compressed, process=process, remove_raw=remove_raw, **kwargs)


@main.command()
@click.argument('dataset')
@click.argument('kwargs', nargs=-1)
@click.pass_context
def clear(ctx, dataset, kwargs):
    "removes the dataset's folder (if it exists) before downloading"

    kwargs = parse_kwargs(kwargs)
    data(dataset, ctx.obj["path"]).clear(**kwargs)

@main.command()
@click.argument('dataset')
@click.option('--clear', '-c', is_flag=True, help="removes the dataset's folder if it exists before downloading")
@click.argument('kwargs', nargs=-1)
@click.pass_context
def download(ctx, dataset, clear, kwargs):
    kwargs = parse_kwargs(kwargs)
    data(dataset, ctx.obj["path"]).download(clear=clear, **kwargs)

@main.command()
@click.argument('dataset')
@click.argument('kwargs', nargs=-1)
@click.pass_context
def extract(ctx, dataset, kwargs):
    kwargs = parse_kwargs(kwargs)
    data(dataset, ctx.obj["path"]).extract(**kwargs)


@main.command()
@click.argument('dataset')
@click.argument('kwargs', nargs=-1)
@click.pass_context
def remove_compressed(ctx, dataset, kwargs):
    kwargs = parse_kwargs(kwargs)
    data(dataset, ctx.obj["path"]).remove_compressed(**kwargs)

@main.command()
@click.argument('dataset')
@click.argument('kwargs', nargs=-1)
@click.pass_context
def process(ctx, dataset, kwargs):
    kwargs = parse_kwargs(kwargs)
    data(dataset, ctx.obj["path"]).process(**kwargs)


@main.command()
@click.argument('dataset')
@click.argument('kwargs', nargs=-1)
@click.pass_context
def remove_raw(ctx, dataset, kwargs):
    kwargs = parse_kwargs(kwargs)
    data(dataset, ctx.obj["path"]).remove_raw(**kwargs)




def parse_kwargs(kwargs):
    return ((dict)((_coconut.functools.partial(map, tuple))((_coconut.functools.partial(map, _coconut.operator.methodcaller("split", "=")))(kwargs))))
