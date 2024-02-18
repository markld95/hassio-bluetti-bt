"""Field attributes for device fields."""

from dataclasses import dataclass
from enum import Enum, auto, unique

from .field_enums import (
    AutoSleepMode,
    ChargingMode,
    EcoShutdown,
    LedMode,
    OutputMode,
    SplitPhaseMachineType,
    UpsMode,
)


@unique
class FieldType(Enum):
    NUMERIC = auto()
    BOOL = auto()
    ENUM = auto()
    BUTTON = auto()


class FieldAttributes:
    def __init__(
        self,
        type: FieldType = FieldType.NUMERIC,
        setter: bool = False,
        name: str = "",
        unit_of_measurement: str | None = None,
        device_class: str | None = None,
        state_class: str | None = None,
        options: Enum | None = None,
    ):
        self.type = type
        self.setter = setter
        self.name = name
        self.unit_of_measurement = unit_of_measurement
        self.device_class = device_class
        self.state_class = state_class
        self.options = options


class PowerFieldAttributes(FieldAttributes):
    def __init__(
        self,
        name: str = "",
    ):
        super().__init__(
            name=name,
            unit_of_measurement="W",
            device_class="power",
            state_class="measurement",
        )


class VoltageFieldAttributes(FieldAttributes):
    def __init__(
        self,
        name: str = "",
    ):
        super().__init__(
            name=name,
            unit_of_measurement="V",
            device_class="voltage",
            state_class="measurement",
        )


class CurrentFieldAttributes(FieldAttributes):
    def __init__(
        self,
        name: str = "",
    ):
        super().__init__(
            name=name,
            unit_of_measurement="A",
            device_class="current",
            state_class="measurement",
        )


class EnergyFieldAttributes(FieldAttributes):
    def __init__(
        self,
        name: str = "",
    ):
        super().__init__(
            name=name,
            unit_of_measurement="kWh",
            device_class="energy",
            state_class="total_increasing",
        )


class FrequencyFieldAttributes(FieldAttributes):
    def __init__(
        self,
        name: str = "",
    ):
        super().__init__(
            name=name,
            unit_of_measurement="Hz",
            device_class="frequency",
            state_class="measurement",
        )


class OutletFieldAttributes(FieldAttributes):
    def __init__(
        self,
        name: str = "",
        setter: bool = False,
    ):
        super().__init__(
            type=FieldType.BOOL,
            name=name,
            setter=setter,
            device_class="outlet",
        )


FIELD_ATTRIBUTES: dict[str, FieldAttributes] = {
    # Base device fields
    "dc_input_power": PowerFieldAttributes(
        name="DC Input Power",
    ),
    "ac_input_power": PowerFieldAttributes(
        name="AC Input Power",
    ),
    "ac_output_power": PowerFieldAttributes(
        name="AC Output Power",
    ),
    "dc_output_power": PowerFieldAttributes(
        name="DC Output Power",
    ),
    "power_generation": EnergyFieldAttributes(
        name="Total Power Generation",
    ),
    "total_battery_percent": FieldAttributes(
        type=FieldType.NUMERIC,
        name="Total Battery Percent",
        unit_of_measurement="%",
        device_class="battery",
        state_class="measurement",
    ),
    "total_battery_voltage": VoltageFieldAttributes(
        name="Total Battery Voltage",
    ),
    "ac_output_on": OutletFieldAttributes(
        name="AC Output",
    ),
    "dc_output_on": OutletFieldAttributes(
        name="DC Output",
    ),
    # Controls
    "ac_output_on_switch": OutletFieldAttributes(
        name="AC Output",
        setter=True,
    ),
    "dc_output_on_switch": OutletFieldAttributes(
        name="DC Output",
        setter=True,
    ),
    # Device specific fields
    "ac_output_mode": FieldAttributes(
        type=FieldType.ENUM,
        name="AC Output Mode",
        options=OutputMode,
    ),
    "internal_ac_voltage": VoltageFieldAttributes(
        name="Internal AC Voltage",
    ),
    "internal_current_one": CurrentFieldAttributes(
        name="Internal Current Sensor 1",
    ),
    "internal_power_one": PowerFieldAttributes(
        name="Internal Power Sensor 1",
    ),
    "internal_ac_frequency": FrequencyFieldAttributes(
        name="Internal AC Frequency",
    ),
    "internal_current_two": CurrentFieldAttributes(
        name="Internal Current Sensor 2",
    ),
    "internal_power_two": PowerFieldAttributes(
        name="Internal Power Sensor 2",
    ),
    "ac_input_voltage": VoltageFieldAttributes(
        name="AC Input Voltage",
    ),
    "internal_current_three": CurrentFieldAttributes(
        name="Internal Current Sensor 3",
    ),
    "internal_power_three": PowerFieldAttributes(
        name="Internal Power Sensor 3",
    ),
    "ac_input_frequency": FrequencyFieldAttributes(
        name="AC Input Frequency",
    ),
    "internal_dc_input_voltage": VoltageFieldAttributes(
        name="Internal DC Input Voltage",
    ),
    "internal_dc_input_power": PowerFieldAttributes(
        name="Internal DC Input Power",
    ),
    "internal_dc_input_current": CurrentFieldAttributes(
        name="Internal DC Input Current",
    ),
    "pv_input_power1": PowerFieldAttributes(
        name="Solar Input Power 1",
    ),
    "pv_input_power2": PowerFieldAttributes(
        name="Solar Input Power 2",
    ),
    "pv_input_voltage1": VoltageFieldAttributes(
        name="Solar Input Voltage 1",
    ),
    "pv_input_voltage2": VoltageFieldAttributes(
        name="Solar Input Voltage 2",
    ),
    "pv_input_current1": CurrentFieldAttributes(
        name="Solar Input Current 1",
    ),
    "pv_input_current2": CurrentFieldAttributes(
        name="Solar Input Current 2",
    ),
    "adl400_ac_input_power_phase1": PowerFieldAttributes(
        name="AC Solar Input Power Phase 1"
    ),
    "adl400_ac_input_power_phase2": PowerFieldAttributes(
        name="AC Solar Input Power Phase 2"
    ),
    "adl400_ac_input_power_phase3": PowerFieldAttributes(
        name="AC Solar Input Power Phase 3"
    ),
    "adl400_ac_input_voltage_phase1": VoltageFieldAttributes(
        name="AC Solar Input Voltage Phase 1",
    ),
    "adl400_ac_input_voltage_phase2": VoltageFieldAttributes(
        name="AC Solar Input Voltage Phase 2",
    ),
    "adl400_ac_input_voltage_phase3": VoltageFieldAttributes(
        name="AC Solar Input Voltage Phase 3",
    ),
    "adl400_ac_input_current_phase1": CurrentFieldAttributes(
        name="AC Solar Input Current Phase 1",
    ),
    "adl400_ac_input_current_phase2": CurrentFieldAttributes(
        name="AC Solar Input Current Phase 2",
    ),
    "adl400_ac_input_current_phase3": CurrentFieldAttributes(
        name="AC Solar Input Current Phase 3",
    ),
    "grid_frequency": FrequencyFieldAttributes(
        name="Grid Frequency",
    ),
    "grid_power_phase1": PowerFieldAttributes(
        name="Grid Power Phase 1",
    ),
    "grid_power_phase2": PowerFieldAttributes(
        name="Grid Power Phase 2",
    ),
    "grid_power_phase3": PowerFieldAttributes(
        name="Grid Power Phase 3",
    ),
    "grid_voltage_phase1": VoltageFieldAttributes(
        name="Grid Voltage Phase 1",
    ),
    "grid_voltage_phase2": VoltageFieldAttributes(
        name="Grid Voltage Phase 2",
    ),
    "grid_voltage_phase3": VoltageFieldAttributes(
        name="Grid Voltage Phase 3",
    ),
    "grid_current_phase1": CurrentFieldAttributes(
        name="Grid Current Phase 1",
    ),
    "grid_current_phase2": CurrentFieldAttributes(
        name="Grid Current Phase 2",
    ),
    "grid_current_phase3": CurrentFieldAttributes(
        name="Grid Current Phase 3",
    ),
    "ac_output_frequency": FrequencyFieldAttributes(
        name="AC Output Frequency",
    ),
    "ac_output_power_phase1": PowerFieldAttributes(
        name="AC Output Power Phase 1",
    ),
    "ac_output_power_phase2": PowerFieldAttributes(
        name="AC Output Power Phase 2",
    ),
    "ac_output_power_phase3": PowerFieldAttributes(
        name="AC Output Power Phase 3",
    ),
    "ac_output_voltage_phase1": VoltageFieldAttributes(
        name="AC Output Voltage Phase 1",
    ),
    "ac_output_voltage_phase2": VoltageFieldAttributes(
        name="AC Output Voltage Phase 2",
    ),
    "ac_output_voltage_phase3": VoltageFieldAttributes(
        name="AC Output Voltage Phase 3",
    ),
    "total_ac_consumption": EnergyFieldAttributes(
        name="Total Load Consumption",
    ),
    "total_grid_consumption": EnergyFieldAttributes(
        name="Total Grid Consumption",
    ),
    "total_grid_feed": EnergyFieldAttributes(
        name="Total Grid Feed",
    ),
    # Device specific controls
    "power_off": FieldAttributes(
        type=FieldType.BUTTON,
        setter=True,
        name="Power Off",
    ),
    "auto_sleep_mode": FieldAttributes(
        type=FieldType.ENUM,
        setter=True,
        name="Screen Auto Sleep Mode",
        options=AutoSleepMode,
    ),
    "ups_mode": FieldAttributes(
        type=FieldType.ENUM,
        setter=False,  # Disabled for safety reasons
        name="UPS Working Mode",
        options=UpsMode,
    ),
    "split_phase_on": FieldAttributes(
        type=FieldType.BOOL,
        setter=False,  # Disabled for safety reasons
        name="Split Phase",
    ),
    "split_phase_machine_mode": FieldAttributes(
        type=FieldType.ENUM,
        setter=False,  # Disabled for safety reasons
        name="Split Phase Machine Type",
        options=SplitPhaseMachineType,
    ),
    "grid_charge_on": FieldAttributes(
        type=FieldType.BOOL,
        setter=False,  # Disabled for safety reasons
        name="Grid Charge",
    ),
    "time_control_on": FieldAttributes(
        type=FieldType.BOOL,
        setter=False,  # Disabled for safety reasons
        name="Time Control",
    ),
    "battery_range_start": FieldAttributes(
        type=FieldType.NUMERIC,
        setter=False,  # Disabled
        name="Battery Range Start",
        unit_of_measurement="%",
    ),
    "battery_range_end": FieldAttributes(
        type=FieldType.NUMERIC,
        setter=False,  # Disabled
        name="Battery Range End",
        unit_of_measurement="%",
    ),
    "led_mode": FieldAttributes(
        type=FieldType.ENUM,
        setter=True,
        name="LED Mode",
        options=LedMode,
    ),
    "eco_on": FieldAttributes(
        type=FieldType.BOOL,
        setter=True,
        name="Eco Mode",
    ),
    "eco_shutdown": FieldAttributes(
        type=FieldType.ENUM,
        setter=True,
        name="Eco Shutdown",
        options=EcoShutdown,
    ),
    "charging_mode": FieldAttributes(
        type=FieldType.ENUM,
        setter=True,
        name="Charging Mode",
        options=ChargingMode,
    ),
    "power_lifting_on": FieldAttributes(
        type=FieldType.BOOL,
        setter=False,  # Disabled for safety reasons
        name="Power Lifting",
    ),
}


def PACK_FIELD_ATTRIBUTES(pack: int):
    return {
        "pack_voltage": VoltageFieldAttributes(
            name=f"Battery Pack {pack} Voltage",
        ),
        "pack_battery_percent": FieldAttributes(
            type=FieldType.NUMERIC,
            name=f"Battery Pack {pack} Percent",
            unit_of_measurement="%",
            device_class="battery",
            state_class="measurement",
        ),
        "pack_bms_version": FieldAttributes(
            type=FieldType.NUMERIC,
            name=f"Battery Pack {pack} BMS Version",
        ),
    }
