from .tokenizer_spec import TokenizerSpec
from pytorch_transformers import GPT2Tokenizer


class NemoGPT2Tokenizer(TokenizerSpec):
    def __init__(self, pretrained_model=None,
                 vocab_file=None, merges_file=None, errors='replace',
                 bos_token="<|endoftext|>",
                 eos_token="<|endoftext|>",
                 **kwargs):
        if pretrained_model:
            self.tokenizer = GPT2Tokenizer.from_pretrained(pretrained_model)
        self.vocab_size = self.tokenizer.vocab_size
        special_tokens_dict = {}
        if self.tokenizer.unk_token is None:
            self.tokenizer.unk_token = "<|unk|>"
            special_tokens_dict["unk_token"] = "<|unk|>"
        if self.tokenizer.bos_token is None:
            special_tokens_dict["bos_token"] = bos_token
        if self.tokenizer.eos_token is None:
            special_tokens_dict["eos_token"] = eos_token
        if self.tokenizer.pad_token is None:
            special_tokens_dict["pad_token"] = "<|pad|>"
        self.tokenizer.add_special_tokens(special_tokens_dict)

    def text_to_tokens(self, text):
        tokens = self.tokenizer.tokenize(text)
        return tokens

    def tokens_to_text(self, tokens):
        text = self.tokenizer.convert_tokens_to_string(tokens)
        return text

    def tokens_to_ids(self, tokens):
        ids = self.tokenizer.convert_tokens_to_ids(tokens)
        return ids

    def ids_to_tokens(self, ids):
        tokens = self.tokenizer.convert_ids_to_tokens(ids)
        return tokens

    def text_to_ids(self, text):
        tokens = self.text_to_tokens(text)
        ids = self.tokens_to_ids(tokens)
        return ids

    def ids_to_text(self, ids):
        tokens = self.ids_to_tokens(ids)
        text = self.tokens_to_text(tokens)
        return text

    def pad_id(self):
        return self.tokens_to_ids([self.tokenizer.pad_token])[0]

    def bos_id(self):
        return self.tokens_to_ids([self.tokenizer.bos_token])[0]

    def eos_id(self):
        return self.tokens_to_ids([self.tokenizer.eos_token])[0]
