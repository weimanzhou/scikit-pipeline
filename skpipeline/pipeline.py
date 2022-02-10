from abc import ABC
from docx import Document
from docx.shared import Inches


class Pipeline(ABC):

    def __init__(self, steps=[], doc=True):
        self.doc = Document() if doc else None
        self.steps = steps

    def fit(self, X, y=None, exraise=None, verbose=False):
        for step in self.steps:
            step.fit(X, y, exraise=exraise, verbose=verbose)

    def transform(self, X, y=None, exraise=None, verbose=False):
        pass

    def fit_transform(self, X, y=None, exraise=None, verbose=False):
        pass
