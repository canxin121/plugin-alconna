from nepattern.main import INTEGER
from arclet.alconna import argv_config, set_default_argv_type
from nepattern import URL, BasePattern, PatternModel, UnionPattern
from nonebot.adapters.villa.message import Message, BaseMessage, MessageSegment

from nonebot_plugin_alconna.argv import MessageArgv
from nonebot_plugin_alconna.typings import SegmentPattern


class VillaMessageArgv(MessageArgv):
    ...


set_default_argv_type(VillaMessageArgv)
argv_config(
    VillaMessageArgv,
    filter_out=[],
    checker=lambda x: isinstance(x, BaseMessage),
    to_text=lambda x: x if x.__class__ is str else str(x) if x.is_text() else None,
    converter=lambda x: Message(x),
)

Text = str
MentionUser = SegmentPattern(
    "mention_user", MessageSegment, MessageSegment.mention_user
)
MentionRobot = SegmentPattern(
    "mention_robot", MessageSegment, MessageSegment.mention_robot
)
MentionAll = SegmentPattern("mention_all", MessageSegment, MessageSegment.mention_all)
RoomLink = SegmentPattern("room_link", MessageSegment, MessageSegment.room_link)
Link = SegmentPattern("link", MessageSegment, MessageSegment.link)
Quote = SegmentPattern("quote", MessageSegment, MessageSegment.quote)
Image = SegmentPattern("image", MessageSegment, MessageSegment.image)
Post = SegmentPattern("post", MessageSegment, MessageSegment.post)
PreviewLink = SegmentPattern(
    "preview_link", MessageSegment, MessageSegment.preview_link
)
Badge = SegmentPattern("badge", MessageSegment, MessageSegment.badge)

ImgOrUrl = (
    UnionPattern(
        [
            BasePattern(
                model=PatternModel.TYPE_CONVERT,
                origin=str,
                converter=lambda _, x: x.data["file_id"],
                alias="img",
                accepts=[Image],
            ),
            URL,
        ]
    )
    @ "img_url"
)
"""
内置类型, 允许传入图片元素(Image)或者链接(URL)，返回链接
"""

MentionID = (
    UnionPattern(
        [
            BasePattern(
                model=PatternModel.TYPE_CONVERT,
                origin=int,
                alias="MentionRobot",
                accepts=[MentionRobot],
                converter=lambda _, x: int(x.data["mention_robot"].bot_id),
            ),
            BasePattern(
                model=PatternModel.TYPE_CONVERT,
                origin=int,
                alias="MentionUser",
                accepts=[MentionUser],
                converter=lambda _, x: int(x.data["mention_user"].user_id),
            ),
            BasePattern(
                r"@(\d+)",
                model=PatternModel.REGEX_CONVERT,
                origin=int,
                alias="@xxx",
                accepts=[str],
            ),
            INTEGER,
        ]
    )
    @ "mention_id"
)
"""
内置类型，允许传入@用户 或者 @机器人 或者'@xxxx'式样的字符串或者数字, 返回数字
"""
