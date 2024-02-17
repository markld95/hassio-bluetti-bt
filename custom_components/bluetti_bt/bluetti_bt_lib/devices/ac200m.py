"""AC200M fields."""

from typing import List

from ..utils.commands import ReadHoldingRegisters
from ..field_enums import AutoSleepMode, OutputMode
from ..base_devices.ProtocolV1Device import ProtocolV1Device


class AC200M(ProtocolV1Device):
    def __init__(self, address: str, sn: str):
        super().__init__(address, "AC200M", sn)

        # Details
        self.struct.add_enum_field('ac_output_mode', 70, OutputMode)
        self.struct.add_uint_field('internal_ac_voltage', 71)
        self.struct.add_decimal_field('internal_current_one', 72, 1)
        self.struct.add_uint_field('internal_power_one', 73)
        self.struct.add_decimal_field('internal_ac_frequency', 74, 1)
        self.struct.add_uint_field('internal_dc_input_voltage', 86)
        self.struct.add_decimal_field('internal_dc_input_power', 87, 1)
        self.struct.add_decimal_field('internal_dc_input_current', 88, 2)

        # Battery packs
        self.struct.add_decimal_array_field('cell_voltages', 105, 16, 2) # internal

        # Controls
        self.struct.add_bool_field('power_off', 3060)
        self.struct.add_enum_field('auto_sleep_mode', 3061, AutoSleepMode)

    @property
    def pack_num_max(self):
        return 3
    
    @property
    def polling_commands(self) -> List[ReadHoldingRegisters]:
        return super().polling_commands + [
            ReadHoldingRegisters(70, 4),
            ReadHoldingRegisters(86, 3),
        ]
    
    @property
    def writable_ranges(self) -> List[range]:
        return super().writable_ranges + [range(3060, 3061)]
    
    @property
    def pack_polling_commands(self) -> List[ReadHoldingRegisters]:
        return super().pack_polling_commands + [ReadHoldingRegisters(105, 16)]
