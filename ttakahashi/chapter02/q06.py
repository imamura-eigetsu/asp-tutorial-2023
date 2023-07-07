from pathlib import Path
from typing import Union
import numpy as np
import matplotlib.pyplot as plt


config = {
    "figure.subplot.bottom": 0.15,
    "figure.subplot.left": 0.15,
    "figure.figsize": [10, 8],
    "font.size": 24,
    "font.family": "Times New Roman",
    "mathtext.fontset": "cm",
    "pdf.fonttype": 42,
    "legend.borderaxespad": 1,
    "lines.linewidth": 2,
    "savefig.transparent": True,
}


def main(output_dir: Union[Path, str]):
    out_p = Path(output_dir)

    A = 1  # amplitude
    f = 440  # frequency (Hz)
    sec = 3  # time (sec)
    sr = 16000  # sampling rate (Hz)

    t = np.arange(sec * sr) / sr
    y = A * np.sin(2 * np.pi * f * t)
    Y = np.fft.fft(y)

    mag_spec = 10 * np.log10(np.abs(Y) ** 2)
    phase_spec = np.angle(Y)
    freq_idx = sr * np.arange(Y.size) / Y.size

    plt.rcParams.update(config)
    fig, ax = plt.subplots(2, 1)
    ax[0].stem(freq_idx, mag_spec)
    ax[0].set_xlim(440 - 10, 440 + 10)
    ax[0].set_title("mag_spec")
    ax[0].grid()
    ax[1].stem(freq_idx, phase_spec)
    ax[1].set_xlim(440 - 10, 440 + 10)
    ax[1].set_title("phase_spec")
    ax[1].grid()
    plt.tight_layout()
    plt.savefig(out_p / "06.pdf")
    plt.clf()
    plt.close()


if __name__ == "__main__":
    out_p = Path.cwd() / "outputs"
    if not out_p.exists():
        out_p.mkdir(parents=True)

    main(out_p)

    print("Finished")