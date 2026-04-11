from sqlalchemy import Column, String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.mutable import MutableDict
from typing import Any, Dict, Optional

from benchmarklib import BaseProblem, BaseTrial, TrialCircuitMetricsMixin, BenchmarkDatabase

class ExperimentProblem(BaseProblem):
    __tablename__ = "experiment_problems"
    TrialClass = "ExperimentTrial"

    n: Mapped[int]
    name: Mapped[str] = Column(String(128), nullable=False, index=True)
    tag: Mapped[Optional[str]] = Column(String(64), nullable=True, index=True)
        
    def number_of_input_bits(self) -> int:
        return self.n

class ExperimentTrial(TrialCircuitMetricsMixin, BaseTrial):
    __tablename__ = "experiment_trials"
    ProblemClass = ExperimentProblem

    compiler_name: Mapped[Optional[str]] = mapped_column(String(255), index=True)  # make optional
    extra_data: Mapped[Dict[str, Any]] = mapped_column(MutableDict.as_mutable(JSON), default=dict)


# export database
db = BenchmarkDatabase("experiments.db", ExperimentProblem, ExperimentTrial)