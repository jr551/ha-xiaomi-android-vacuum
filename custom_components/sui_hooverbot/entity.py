"""Shared entity helpers for Litter Tray Vacuum Cleanup."""

from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, INTEGRATION_NAME
from .runtime import SuiRuntime


class SuiEntity(CoordinatorEntity):
    """A recorder-safe entity backed by the cleanup coordinator."""

    _attr_has_entity_name = True

    def __init__(self, runtime: SuiRuntime, suffix: str) -> None:
        super().__init__(runtime.coordinator)
        self.runtime = runtime
        self._attr_unique_id = f"{runtime.entry.entry_id}_{suffix}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, runtime.entry.entry_id)},
            name=INTEGRATION_NAME,
            manufacturer="Home Assistant",
            model="Litter-tray vacuum scheduler",
        )

    @property
    def schedule_data(self) -> dict[str, object]:
        return self.coordinator.data or self.runtime.snapshot()
