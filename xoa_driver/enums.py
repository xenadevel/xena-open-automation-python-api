"""
Avaliable enums used by commands abd response status.
"""

from .internals.core.commands.enums import *
from .internals.core.protocol.constants import CommandStatus

__all__ = (
    "ReservedStatus",
    "ReservedAction",
    "ChassisShutdownAction",
    "OnOff",
    "RESTControlAction",
    "ServiceStatus",
    "ChassisSessionType",
    "TimeSyncMode",
    "CFPState",
    "CFPType",
    "SMAInputFunction",
    "SMAOutputFunction",
    "SMAStatus",
    "HasDemo",
    "IsValid",
    "IsPermanent",
    "YesNo",
    "UpdateState",
    "IsOnline",
    "PortSpeedMode",
    "SyncStatus",
    "LoopMode",
    "TrafficOnOff",
    "StartOrStop",
    "LatencyMode",
    "SourceType",
    "PacketDetailSelection",
    "OnOffWithSuppress",
    "ProtocolOption",
    "ModifierAction",
    "LengthType",
    "PayloadType",
    "MDIXMode",
    "LengthCheckType",
    "StartTrigger",
    "StopTrigger",
    "PacketType",
    "InjectErrorType",
    "HeaderLockStatus",
    "AlignLockStatus",
    "PRBSLockStatus",
    "MulticastOperation",
    "MulticastExtOperation",
    "IGMPVersion",
    "LoopbackMode",
    "PayloadMode",
    "BRRMode",
    "TXClock",
    "TXClockStatus",
    "FilterBandwidth",
    "MediaType",
    "TXHState",
    "RXHState",
    "TXCState",
    "RXCState",
    "LinkState",
    "FaultSignaling",
    "LocalFaultStatus",
    "RemoteFaultStatus",
    "TPLDMode",
    "SerdesStatus",
    "FECMode",
    "PRBSInsertedType",
    "PRBSPolynomial",
    "PRBSInvertState",
    "PRBSStatisticsMode",
    "AutoNegMode",
    "AutoNegTecAbility",
    "AutoNegFecOption",
    "PauseMode",
    "AutoNegFECType",
    "AutoNegStatus",
    "AutoNegStatusFEC",
    "LinkTrainMode",
    "PAM4FrameSize",
    "LinkTrainingInitCondition",
    "NRZPreset",
    "TimeoutMode",
    "LinkTrainingMode",
    "LinkTrainStatus",
    "LinkTrainFailureType",
    "Role",
    "Timescale",
    "MssType",
    "RtoType",
    "CongestionType",
    "IsEnabled",
    "AlgorithmMethod",
    "AutoOrManual",
    "EmbedIP",
    "ApplicationLayerBehavior",
    "TrafficScenario",
    "PayloadGenerationMethod",
    "InfiniteOrFinite",
    "WhoClose",
    "LifecycleMode",
    "IPVersion",
    "ProtocolType",
    "TrafficState",
    "PortState",
    "PortSpeed",
    "CaptureSize",
    "ReplayParserState",
    "IsPresent",
    "LicenseSpeed",
    "TLSVersion",
    "HeaderFormat",
    "Infinite",
    "CorruptionType",
    "PolicerMode",
    "EthernetInfo",
    "Clude",
    "L2PlusPresent",
    "L3PlusPresent",
    "Flow",
    "TimeKeeperLicenseFileState",
    "TimeKeeperLicenseType",
    "TimeKeeperLicenseError",
    "SystemUpdateStatus",
    "TimeKeeperServiceStatus",
    "TimeKeeperServiceAction",
    "CustomeDefaultCommand",
    "CustomeDefaultScope",
    "NORMAL_EXTENDED",
    "ResourceAllocationMode",
    "BANDWIDTH_TIME",
    "PER_CONN_PER_USER",
    "TrafficError",
    "PRBSOnOff",
    "ErrorOnOff",
    "PRBSPattern",
    "PHYSignalStatus",
    "ShadowWorkingSelection",
    "TSNConfigProfile",
    "TSNPortRole",
    "TSNDeviationMode",
    "TSNTimeSource",
    "TSNSource",
    "TSNClearStatistics",
    "PFCMode",
    "OnOffDefault",
    "ImpairmentTypeIndex",
    "FilterType",
    "VlanType",
    "LatencyType",
    "CommandStatus",
)