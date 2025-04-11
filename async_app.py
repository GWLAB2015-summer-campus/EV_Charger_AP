import asyncio

from kivymd.app import MDApp

class AsyncApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gather = None
        self.other_tasks = []

    def app_func(self):
        async def run_wrapper():
            await self.async_run(async_lib="asyncio")
            for task in self.other_tasks:
                task.close()
        
        self.gather = asyncio.gather(run_wrapper(), *self.other_tasks)
        return self.gather
    
    def add_async_task(self, task, loading=True):
        if loading:
            from view import LoadingView

            loading_view = LoadingView()
            self.root.add_widget(
                loading_view
            )

        self.other_tasks.append(task)

        async def loading_for_task():
            from log_helper import log
            log(f"Running Task Async : {task.__name__}")
            await task
            self.other_tasks.remove(task)
            log(f"Task Finished : {task.__name__}")
            if loading:
                self.root.remove_widget(loading_view)
                
        self.gather = asyncio.gather(self.gather, loading_for_task())