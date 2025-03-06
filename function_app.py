import logging
import azure.functions as func
import jinja2
#If you uncomment the line below, the Azure Function app will no longer able to find the function 'timer_trigger' anymore.
#The log message below has been seen in the Azure function
#No job functions found. Try making your job classes and methods public. If you're using binding extensions (e.g. Azure Storage, ServiceBus, Timers, etc.) make sure you've called the registration method for the extension(s) in your startup code (e.g. builder.AddAzureStorage(), builder.AddServiceBus(), builder.AddTimers(), etc.).
#import numpy


app = func.FunctionApp()

@app.schedule(schedule="*/1 * * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False)
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')