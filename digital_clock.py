#!/usr/bin/env python3
"""
Digital Clock - Multi-Timezone Display
A simple application to display current time in different time zones.
"""

import tkinter as tk
from tkinter import font
from datetime import datetime
import pytz
from typing import List, Dict


class DigitalClock:
    """A digital clock that displays time in multiple time zones."""
    
    def __init__(self, root: tk.Tk, timezones: List[str]):
        """
        Initialize the digital clock.
        
        Args:
            root: Tkinter root window
            timezones: List of timezone strings (e.g., ['UTC', 'US/Eastern', 'Asia/Tokyo'])
        """
        self.root = root
        self.root.title("Digital Clock - Multi-Timezone")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        self.timezones = timezones
        self.timezone_labels = {}
        self.time_labels = {}
        
        self.setup_ui()
        self.update_time()
    
    def setup_ui(self) -> None:
        """Setup the user interface for the clock."""
        # Title
        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        title_label = tk.Label(
            self.root,
            text="Multi-Timezone Digital Clock",
            font=title_font,
            fg="#00ff00",
            bg="#1e1e1e"
        )
        title_label.pack(pady=10)
        
        # Clock frame
        clock_frame = tk.Frame(self.root, bg="#1e1e1e")
        clock_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Create clock display for each timezone
        for i, tz in enumerate(self.timezones):
            # Timezone name
            tz_font = font.Font(family="Courier", size=12, weight="bold")
            tz_label = tk.Label(
                clock_frame,
                text=tz,
                font=tz_font,
                fg="#00ff00",
                bg="#1e1e1e"
            )
            tz_label.pack(anchor=tk.W, pady=5)
            self.timezone_labels[tz] = tz_label
            
            # Time display
            time_font = font.Font(family="Courier", size=24, weight="bold")
            time_label = tk.Label(
                clock_frame,
                text="00:00:00",
                font=time_font,
                fg="#00ff00",
                bg="#0a0a0a",
                padx=10,
                pady=5
            )
            time_label.pack(anchor=tk.W, pady=5, fill=tk.X, padx=5)
            self.time_labels[tz] = time_label
        
        # Info label
        info_font = font.Font(family="Helvetica", size=9)
        info_label = tk.Label(
            self.root,
            text="Click 'Exit' to close the application",
            font=info_font,
            fg="#888888",
            bg="#1e1e1e"
        )
        info_label.pack(pady=5)
        
        # Exit button
        exit_button = tk.Button(
            self.root,
            text="Exit",
            command=self.root.quit,
            bg="#00ff00",
            fg="#000000",
            font=("Helvetica", 10, "bold"),
            padx=20,
            pady=5
        )
        exit_button.pack(pady=10)
    
    def update_time(self) -> None:
        """Update the time display for all timezones."""
        for tz in self.timezones:
            try:
                # Get current time in the timezone
                timezone = pytz.timezone(tz)
                current_time = datetime.now(timezone)
                time_string = current_time.strftime("%H:%M:%S")
                
                # Update the label
                self.time_labels[tz].config(text=time_string)
            except Exception as e:
                self.time_labels[tz].config(text=f"Error: {str(e)}")
        
        # Schedule next update after 1000 milliseconds (1 second)
        self.root.after(1000, self.update_time)


def main():
    """Main function to run the digital clock application."""
    # Define timezones to display
    timezones = [
        'UTC',
        'US/Eastern',
        'US/Central',
        'US/Mountain',
        'US/Pacific',
        'Europe/London',
        'Europe/Paris',
        'Asia/Tokyo',
        'Asia/Shanghai',
        'Australia/Sydney'
    ]
    
    root = tk.Tk()
    clock = DigitalClock(root, timezones)
    root.mainloop()


if __name__ == "__main__":
    main()
