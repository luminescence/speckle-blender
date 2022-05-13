from .users import LoadUsers, LoadUserStreams
from .object import (
    UpdateObject,
    ResetObject,
    DeleteObject,
    UploadNgonsAsPolylines,
    SelectIfSameCustomProperty,
    SelectIfHasCustomProperty,
    ToggleSpectionary,
)
from .streams import (
    ReceiveStreamObjects,
    SendStreamObjects,
    ViewStreamDataApi,
    DeleteStream,
    SelectOrphanObjects,
)
from .streams import (
    UpdateGlobal,
    AddStreamFromURL,
    CreateStream,
    CopyStreamId,
    CopyCommitId,
    CopyBranchName,
)
from .commit import DeleteCommit
from .misc import OpenSpeckleGuide, OpenSpeckleTutorials, OpenSpeckleForum

operator_classes = [
    LoadUsers,
    ReceiveStreamObjects,
    SendStreamObjects,
    LoadUserStreams,
    CopyStreamId,
    CopyCommitId,
    CopyBranchName,
]

operator_classes.extend([DeleteCommit])

operator_classes.extend(
    [
        UpdateObject,
        ResetObject,
        DeleteObject,
        UploadNgonsAsPolylines,
        SelectIfSameCustomProperty,
        SelectIfHasCustomProperty,
        ToggleSpectionary,
    ]
)

operator_classes.extend(
    [
        ViewStreamDataApi,
        DeleteStream,
        SelectOrphanObjects,
        UpdateGlobal,
        AddStreamFromURL,
        CreateStream,
        OpenSpeckleGuide,
        OpenSpeckleTutorials,
        OpenSpeckleForum,
    ]
)
