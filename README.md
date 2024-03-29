# python-3.10-vs-3.11-exception-analysis

This repository contains a analysis comparing exception handling performance between Python 3.10 and Python 3.11, focusing on the "zero-cost exceptions" feature introduced in Python 3.11.

## Background

The introduction of "zero-cost exceptions" in Python 3.11 aimed to eliminate the performance cost of `try` statements when no exception is raised. For more detailed information, refer to the [Python 3.11 release notes](https://docs.python.org/3/whatsnew/3.11.html#misc).

However, there has been discussion regarding the actual cost of exceptions when they are thrown, suggesting that "zero-cost" might not be entirely without performance implications. For an in-depth analysis, see this article from Microsoft's developer blog: ["Zero-cost exceptions aren’t actually zero cost"](https://devblogs.microsoft.com/oldnewthing/20220228-00/?p=106296).

## Test Environment 
OS: Microsoft Windows Version 22H2 (OS Build 19045.4170)
CPU: AMD Ryzen 7 5800H
RAM: 16GB DDR4, 3200MHz SODIMM
Storage: SHGP31-1000GM-2 NVMe PCIe SSD
Python version: 3.10.0, 3.11.0