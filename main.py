import logging
import logging.config
import tkinter as tk


def setup_logging():
    """Configure logging from file."""
    logging.config.fileConfig('logging.conf')


def show_message():
    """Display a window with a greeting."""
    logger = logging.getLogger(__name__)
    logger.info('Starting GUI application')
    try:
        root = tk.Tk()
        root.title('Greeting')
        label = tk.Label(root, text='Hello, world!')
        label.pack()
        logger.info('Running main loop')
        root.mainloop()
    except tk.TclError as exc:
        logger.error('Unable to display window: %s', exc)


if __name__ == '__main__':
    setup_logging()
    show_message()

