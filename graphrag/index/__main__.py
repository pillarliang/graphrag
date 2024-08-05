# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""The Indexing Engine package root."""

import argparse
import uuid

import pandas as pd
from graphrag.query.cli import run_local_search

from graphrag.index.cli import index_cli

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        help="The configuration yaml file to use when running the pipeline",
        required=False,
        type=str,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Runs the pipeline with verbose logging",
        action="store_true",
    )
    parser.add_argument(
        "--memprofile",
        help="Runs the pipeline with memory profiling",
        action="store_true",
    )
    parser.add_argument(
        "--root",
        help="If no configuration is defined, the root directory to use for input data and output data. Default value: the current directory",
        # Only required if config is not defined
        required=False,
        default=".",
        type=str,
    )
    parser.add_argument(
        "--resume",
        help="Resume a given data run leveraging Parquet output files.",
        # Only required if config is not defined
        required=False,
        default=None,
        type=str,
    )
    parser.add_argument(
        "--reporter",
        help="The progress reporter to use. Valid values are 'rich', 'print', or 'none'",
        type=str,
    )
    parser.add_argument(
        "--emit",
        help="The data formats to emit, comma-separated. Valid values are 'parquet' and 'csv'. default='parquet,csv'",
        type=str,
    )
    parser.add_argument(
        "--dryrun",
        help="Run the pipeline without actually executing any steps and inspect the configuration.",
        action="store_true",
    )
    parser.add_argument("--nocache", help="Disable LLM cache.", action="store_true")
    parser.add_argument(
        "--init",
        help="Create an initial configuration in the given path.",
        action="store_true",
    )
    parser.add_argument(
        "--overlay-defaults",
        help="Overlay default configuration values on a provided configuration file (--config).",
        action="store_true",
    )
    args = parser.parse_args()

    if args.overlay_defaults and not args.config:
        parser.error("--overlay-defaults requires --config")
    data = [{
        "title": "d1",
        "text": """
            No.2 广州-潘倩祺_原文
2024年07月17日 10:50
发言人1   00:11
好，那我们俩访问就讲普通话，因为只有我会讲白话。他们俩。好，可以先跟你说一下，为什么今天有这个活动，我也不知道你今天有参加过。我们是专门做市场调研的，然后公司经常会做很多不同的项目，有时候会做一些美妆类的，然后就想要知道说现在大家都化妆这样子，然后也是可能做一些汽车的项目的。你就看一下现在大家对于汽车的一些设计的想法是什么。

发言人1   00:39
那今天之前也问过你，平时洗护类的产品，包括你的洗澡这些东西，对我们就是比较感兴趣。想要知道说你平时是怎么挑这些东西，包括说你洗护的这个习惯是怎么样子的。所以这东西没有什么对与错的，就是每个人的习惯不太一样。所以就想来问问你，可能因为有些东西我可能又比较仔细，可能需要多让你多说一点，然后就是有些细节的东西。

发言人1   01:05
好的，行，那整个跑步大概就是2个小时。我想先问一下你就是是刚毕业不久吗？什么时候毕业的？前年，现在一直都是住在家里。

潘倩祺   01:19
对，就是跟爸妈一起住的。

发言人1   01:22
从小到大的事之后有想过要搬出去吗？

潘倩祺   01:28
暂时还没有想法，以后就不好说。

发言人1   01:30
就这样，然后一直都是住在这边的那平时平时你有什么兴趣安排。

潘倩祺   01:37
有兴趣爱好的话去旅游，然后去逛街，有时候探店打卡一些美食，然后可能打游戏。

发言人1   01:46
他的也那平时你比如说运动什么的，这样好的。

潘倩祺   01:51
运动可能比较少，我可能就是只想主要是出去旅游那些比较多一些。

发言人1   01:58
如果我问你，就是你觉得自己属于什么肤质，你会怎么评判自己的肤质？

潘倩祺   02:06
我脸部的话就是会有，然后身体的话可能就是中性这样子。
潘倩祺   03:29
但是我是特地说是手是这样子，但是其他身体部位的话就使用身体乳就可以了。

发言人1   03:36
这个手是你自己觉得干，还是说你看到有起皮。

潘倩祺   03:39
或者是自己觉得干，但是它没有说起皮什么的，自己会感觉到紧绷感。对，就是那种紧绷感。

发言人1   03:47
让我很不适，我就觉得，所以每次洗完都会去涂。的对。

潘倩祺   03:52
可能在公司的话我可能就是涂普通的护手霜。对，然后可能晚上睡觉之前我就会涂凡士林，因为它可能睡觉的时间比较久，有一些然后可能凡士林它比较厚重一些的话，它的保湿那个效果就会好一些。

发言人1   04:05
我觉得就等于敷了一个手膜。对对对，晚上的那种，所以就是手跟脚而已，身体其他的地方都没有。

潘倩祺   04:12
身体其他地方我就普通的身体乳加身体油这样。

发言人1   04:17
你一直以来都是这样子吗？对，从小就开始。

潘倩祺   04:23
可能是高中这样子，然后就开始。对，然后无论是一年四季就不分说夏天冬天这样。那可能夏天晚上的话我就不会用凡士林。

发言人1   04:35
就可能是冬天的身体乳就可以了。

潘倩祺   04:37
对。

发言人1   04:37
然后冬天的话可能就会用凡士林。冬天凡士林是就是手跟脚对身体其实没什么的对。我问一下好奇，你刚刚说从高中开始你会关注这个，就会觉得自己开始会有这个习惯。你是什么家里人教你的还是？

潘倩祺   04:56
潘倩祺   07:03
就是我要拿出来吗？

发言人1   07:04
还是你我进去也可以。

潘倩祺   07:20
然后这个就是平时反正用的身体乳都是一直用50个. 

发言人1   07:26
能把东西排出来。看看，这个是你的身体，我刚刚说的，然后那个身体乳是美白的，那个身体我刚刚讲的。对你怎么会想到用油？因为美白也有很多身体乳是美白的。你为什么会想要买一个油？

潘倩祺   07:39
因为我之前有买过很多不同品牌的身就是。
        """,
        "id": str(uuid.uuid4())
    }]
    dataset = pd.DataFrame(data)
    index_cli(
        root=args.root,
        dataset=dataset,
        verbose=args.verbose or False,
        resume=args.resume,
        memprofile=args.memprofile or False,
        nocache=args.nocache or False,
        reporter=args.reporter,
        config=args.config,
        emit=args.emit,
        dryrun=args.dryrun or False,
        init=args.init or False,
        overlay_defaults=args.overlay_defaults or False,
        cli=True,
    )

    res = run_local_search(data_dir=None, root_dir="/Users/liangzhu/Documents/dev/ai/project/graphrag/ragtest", query="受访者对于洗护产品的见解？")
    # print(res)