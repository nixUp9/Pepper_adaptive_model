<?xml version="1.0" encoding="UTF-8" ?>
<Package name="Thesis robot" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
        <Dialog name="helloWorld" src="helloWorld/helloWorld.dlg" />
    </Dialogs>
    <Resources>
        <File name="heaven1" src="behavior_1/behavior_1/heaven1.ogg" />
        <File name="golf" src="behavior_1/golf.ogg" />
        <File name="epicsax" src="behavior_1/epicsax.ogg" />
    </Resources>
    <Topics>
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" />
        <Topic name="helloWorld_enu" src="helloWorld/helloWorld_enu.top" topicName="helloWorld" language="en_US" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
