from dataclasses import dataclass, field


@dataclass
class Message:
    role: str
    content: str


@dataclass
class Conversation:

    messages: list[Message] = field(default_factory=list)

    def add_system(self, text):

        self.messages.append(
            Message("system", text)
        )

    def add_user(self, text):

        self.messages.append(
            Message("user", text)
        )

    def add_assistant(self, text):

        self.messages.append(
            Message("assistant", text)

        )

    def to_openai(self):

        return [

            {

                "role": m.role,

                "content": m.content,

            }

            for m in self.messages

        ]