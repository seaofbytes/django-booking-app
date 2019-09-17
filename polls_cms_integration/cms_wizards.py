from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from polls_cms_integration.forms import PollWizardForm


class PollWizard(Wizard):
    pass


poll_wizard = PollWizard(
    title="Poll",
    weight=200,  # determines the ordering of wizards in the Create dialog
    form=PollWizardForm,
    description="Create a new Poll",
)

wizard_pool.register(poll_wizard)
