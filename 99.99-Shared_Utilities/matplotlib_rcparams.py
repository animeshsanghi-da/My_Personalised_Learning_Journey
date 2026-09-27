import matplotlib as mpl
import matplotlib.pyplot as plt

# ==============================================================================
# MASTER MATPLOTLIB RCPARAMS CONFIGURATION TEMPLATE
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. FIGURE & CANVAS LAYOUT
# ------------------------------------------------------------------------------
mpl.rcParams['figure.figsize'] = (10, 6)       # Default figure dimensions (width, height) in inches
mpl.rcParams['figure.dpi'] = 100               # Screen display resolution in dots per inch
mpl.rcParams['figure.facecolor'] = '#ffffff'   # Outer canvas background color
mpl.rcParams['figure.edgecolor'] = '#ffffff'   # Outer canvas border color
mpl.rcParams['figure.autolayout'] = True       # Auto-adjust layout to prevent label overlap (tight_layout)
mpl.rcParams['figure.titlesize'] = 16          # Font size for top-level super titles (fig.suptitle)

# ------------------------------------------------------------------------------
# 2. AXES & PLOT FRAMES
# ------------------------------------------------------------------------------
mpl.rcParams['axes.facecolor'] = '#f4f4f4'     # Background fill color of the plot area
mpl.rcParams['axes.edgecolor'] = '#cccccc'     # Frame border line color
mpl.rcParams['axes.linewidth'] = 1.2           # Thickness of the plot frame border lines
mpl.rcParams['axes.titlesize'] = 18            # Subplot title font size
mpl.rcParams['axes.titleweight'] = 'bold'      # Subplot title font weight ('normal', 'bold', etc.)
mpl.rcParams['axes.titlepad'] = 12             # Vertical space/padding between title and plot top
mpl.rcParams['axes.labelsize'] = 11            # Font size for X and Y axis titles
mpl.rcParams['axes.labelweight'] = 'bold'      # Font weight for X and Y axis titles
mpl.rcParams['axes.labelcolor'] = '#333333'     # Text color for X and Y axis labels
mpl.rcParams['axes.spines.top'] = False        # Remove top border spine by default
mpl.rcParams['axes.spines.right'] = False      # Remove right border spine by default
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(  # Default color palette cycle for multi-series plots
    color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
)

# ------------------------------------------------------------------------------
# 3. TYPOGRAPHY & TEXT
# ------------------------------------------------------------------------------
mpl.rcParams['font.family'] = 'sans-serif'     # Base font family ('sans-serif', 'serif', 'monospace')
mpl.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial'] # Priority fallback list for sans-serif
mpl.rcParams['font.size'] = 10                 # Global default baseline font size
mpl.rcParams['text.color'] = '#222222'         # Color for generic annotations and text boxes
mpl.rcParams['text.usetex'] = False            # Set to True if using external system LaTeX installation

# ------------------------------------------------------------------------------
# 4. LINES, MARKERS & PATCHES
# ------------------------------------------------------------------------------
mpl.rcParams['lines.linewidth'] = 3            # Default line thickness for plt.plot()
mpl.rcParams['lines.linestyle'] = '-'          # Default line pattern ('-', '--', '-.', ':')
mpl.rcParams['lines.marker'] = 'none'          # Default marker symbol ('o', 's', '^', 'none')
mpl.rcParams['lines.markersize'] = 6           # Default marker size when markers are enabled
mpl.rcParams['lines.antialiased'] = True       # Enable line smoothing algorithm to reduce jaggedness
mpl.rcParams['patch.linewidth'] = 1.0          # Border width for bar charts, histograms, and patches
mpl.rcParams['patch.edgecolor'] = '#ffffff'     # Border line color surrounding bar chart columns

# ------------------------------------------------------------------------------
# 5. TICKS & AXIS SCALES
# ------------------------------------------------------------------------------
mpl.rcParams['xtick.direction'] = 'out'        # X-tick mark orientation ('in', 'out', 'inout')
mpl.rcParams['xtick.major.size'] = 6           # Length of major tick lines on X-axis (in points)
mpl.rcParams['xtick.major.width'] = 1.0         # Thickness of X-axis major tick lines
mpl.rcParams['xtick.labelsize'] = 10           # Font size of X-axis tick numbers/labels
mpl.rcParams['xtick.color'] = '#333333'        # Color applied to X ticks and their numeric labels

mpl.rcParams['ytick.direction'] = 'out'        # Y-tick mark orientation ('in', 'out', 'inout')
mpl.rcParams['ytick.major.size'] = 6           # Length of major tick lines on Y-axis (in points)
mpl.rcParams['ytick.major.width'] = 1.0         # Thickness of Y-axis major tick lines
mpl.rcParams['ytick.labelsize'] = 10           # Font size of Y-axis tick numbers/labels
mpl.rcParams['ytick.color'] = '#333333'        # Color applied to Y ticks and their numeric labels

# ------------------------------------------------------------------------------
# 6. GRIDS & LEGENDS
# ------------------------------------------------------------------------------
mpl.rcParams['axes.grid'] = True               # Automatically show grid lines on all new plots
mpl.rcParams['grid.color'] = '#cccccc'         # Color of background grid lines
mpl.rcParams['grid.linestyle'] = '--'          # Pattern of grid lines ('-', '--', ':', etc.)
mpl.rcParams['grid.linewidth'] = 0.8           # Thickness of grid lines
mpl.rcParams['grid.alpha'] = 0.7               # Grid opacity (0.0 = invisible, 1.0 = solid)

mpl.rcParams['legend.loc'] = 'best'            # Automatic optimal positioning for chart legends
mpl.rcParams['legend.fontsize'] = 10           # Font size for legend label text
mpl.rcParams['legend.frameon'] = True          # Enable background container box around legend
mpl.rcParams['legend.facecolor'] = '#ffffff'   # Fill color inside legend container box
mpl.rcParams['legend.edgecolor'] = '#cccccc'   # Border color of legend container box
mpl.rcParams['legend.shadow'] = False          # Enable or disable drop-shadow behind legend box

# ------------------------------------------------------------------------------
# 7. HEATMAPS, IMAGES & 2D SURFACES
# ------------------------------------------------------------------------------
mpl.rcParams['image.cmap'] = 'viridis'         # Default colormap for heatmaps, imshow(), and hexbin
mpl.rcParams['image.interpolation'] = 'nearest' # Pixel blending method for rendering image arrays
mpl.rcParams['image.origin'] = 'upper'         # Set array origin placement ('upper' vs 'lower' left)

# ------------------------------------------------------------------------------
# 8. EXPORT & SAVING DEFAULTS (plt.savefig)
# ------------------------------------------------------------------------------
mpl.rcParams['savefig.dpi'] = 300              # Export resolution for high-res images (DPI)
mpl.rcParams['savefig.format'] = 'png'         # Default file output format ('png', 'pdf', 'svg')
mpl.rcParams['savefig.bbox'] = 'tight'         # Crop extra surrounding whitespace on export
mpl.rcParams['savefig.pad_inches'] = 0.1       # Margin padding retained after tight-cropping
mpl.rcParams['savefig.transparent'] = False   # Retain background color on export (False = opaque)

# ------------------------------------------------------------------------------
# 9. INTERACTIVE BACKENDS & KEYMAPS
# ------------------------------------------------------------------------------
# mpl.rcParams['backend'] = 'QtAgg'           # GUI backend renderer ('QtAgg', 'TkAgg', 'inline')
mpl.rcParams['keymap.save'] = ['s', 'ctrl+s']  # Interactive window hotkeys to save current figure